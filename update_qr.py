#!/usr/bin/env python3
"""
Automated QR Code Updater for Birthday Surprise
Updates the QR code with the actual GitHub Pages URL after hosting.
"""

import qrcode
from PIL import Image
import os
import sys

def update_qr_code(username):
    """
    Update QR code with the actual GitHub Pages URL.
    """
    try:
        # URL for the birthday surprise webpage
        url = f"https://{username}.github.io/BirthdaySurprise/index.html"
        
        print("🎉 Updating QR Code with GitHub Pages URL 🎉")
        print("=" * 50)
        print(f"GitHub Pages URL: {url}")
        print()
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size in boxes
        )
        
        # Add data to QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code
        output_filename = "surprise_qr.png"
        qr_image.save(output_filename)
        
        # Verify the file was created
        if os.path.exists(output_filename):
            file_size = os.path.getsize(output_filename)
            print(f"✅ QR code successfully updated!")
            print(f"📁 File: {output_filename}")
            print(f"📏 Size: {file_size} bytes")
            print()
            print("🎯 Your surprise is ready!")
            print(f"🌐 Webpage: {url}")
            print("📱 QR Code: surprise_qr.png")
            print()
            print("🎊 Share the QR code with your friend!")
            print("   They can scan it with their phone's camera")
            print("   to see the amazing birthday surprise!")
            
        else:
            print("❌ Error: QR code file was not created successfully")
            return False
            
    except ImportError as e:
        print("❌ Error: Required libraries not installed")
        print("Please install the required libraries:")
        print("pip install qrcode[pil]")
        return False
        
    except Exception as e:
        print(f"❌ Error updating QR code: {str(e)}")
        return False
    
    return True

def main():
    """
    Main function to update the QR code.
    """
    if len(sys.argv) != 2:
        print("Usage: python update_qr.py <github_username>")
        print("Example: python update_qr.py john")
        return
    
    username = sys.argv[1]
    
    # Update the QR code
    success = update_qr_code(username)
    
    if success:
        print("🎊 QR code update completed successfully!")
        print("Ready to share with your friend!")
    else:
        print("💔 QR code update failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
