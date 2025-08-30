#!/usr/bin/env python3
"""
Download all images referenced in TTFM course markdown files
Organizes them by section and maintains folder structure
"""

import os
import re
import requests
from pathlib import Path
import time

def extract_images_from_md(file_path):
    """Extract image URLs from markdown file"""
    images = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all image references: ![](url) or [](url)
        image_pattern = r'\[.*?\]\((https://imagedelivery\.net/[^)]+)\)'
        matches = re.findall(image_pattern, content)
        
        for match in matches:
            images.append(match)
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return images

def download_image(url, save_path, max_retries=3):
    """Download image with retry logic"""
    for attempt in range(max_retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            with open(save_path, 'wb') as f:
                f.write(response.content)
                
            print(f"✅ Downloaded: {os.path.basename(save_path)}")
            return True
            
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
                
    return False

def main():
    base_dir = Path("c:/Users/dbruc/workspace/MyICTConcepts/TradingSystemNotes/ttfm_course")
    
    if not base_dir.exists():
        print(f"❌ Course directory not found: {base_dir}")
        return
        
    # Find all markdown files
    md_files = list(base_dir.rglob("*.md"))
    print(f"📚 Found {len(md_files)} markdown files")
    
    total_images = 0
    downloaded_images = 0
    
    for md_file in md_files:
        print(f"\n📖 Processing: {md_file.name}")
        images = extract_images_from_md(md_file)
        
        if not images:
            print("   No images found")
            continue
            
        # Create images folder in same directory as markdown file
        images_dir = md_file.parent / "images"
        
        print(f"   Found {len(images)} images")
        total_images += len(images)
        
        for i, url in enumerate(images, 1):
            # Generate filename from URL or use sequential numbering
            url_parts = url.split('/')
            if len(url_parts) > 1:
                filename = f"{url_parts[-2]}.png"  # Use UUID as filename
            else:
                filename = f"image_{i:02d}.png"
                
            save_path = images_dir / filename
            
            # Skip if already exists
            if save_path.exists():
                print(f"   ⏭️  Skipping existing: {filename}")
                downloaded_images += 1
                continue
                
            print(f"   ⬇️  Downloading {i}/{len(images)}: {filename}")
            if download_image(url, save_path):
                downloaded_images += 1
                time.sleep(1)  # Be respectful to the server
                
    print(f"\n🎉 Complete! Downloaded {downloaded_images}/{total_images} images")
    
    # Update markdown files with local image references
    print("\n📝 Updating markdown files with local references...")
    for md_file in md_files:
        update_markdown_references(md_file)

def update_markdown_references(md_file):
    """Update markdown files to reference local images"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace remote URLs with local paths
        def replace_url(match):
            url = match.group(1)
            url_parts = url.split('/')
            if len(url_parts) > 1:
                filename = f"{url_parts[-2]}.png"
                return f'[](.images/{filename})'
            return match.group(0)
            
        # Find and replace image URLs
        image_pattern = r'\[.*?\]\((https://imagedelivery\.net/[^)]+)\)'
        updated_content = re.sub(image_pattern, replace_url, content)
        
        if updated_content != content:
            # Create backup
            backup_path = str(md_file) + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            # Write updated content
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
                
            print(f"   ✅ Updated references in {md_file.name}")
            
    except Exception as e:
        print(f"   ❌ Error updating {md_file.name}: {e}")

if __name__ == "__main__":
    main()
