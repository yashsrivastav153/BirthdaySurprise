#!/usr/bin/env python3
"""
Birthday Surprise QR Code Generator
Generates a QR code that links to the birthday surprise webpage with enhanced animations.
Includes hearts tree, cake, candles blow, and confetti effects.
"""

import qrcode
from PIL import Image
import os
import sys

def generate_qr_code():
    """
    Generate a QR code for the birthday surprise webpage.
    """
    try:
        # URL for the birthday surprise webpage
        # Replace 'YOUR_USERNAME' with your actual GitHub username after hosting
        url = "https://yashsrivastav153.github.io/BirthdaySurprise/index.html"
        
        print("🎉 Birthday Surprise QR Code Generator 🎉")
        print("=" * 50)
        print(f"Generating QR code for: {url}")
        print("Note: Replace 'YOUR_USERNAME' with your actual GitHub username")
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
            print(f"✅ QR code successfully generated!")
            print(f"📁 File: {output_filename}")
            print(f"📏 Size: {file_size} bytes")
            print()
            print("🎯 Next Steps:")
            print("1. Host your index.html on GitHub Pages")
            print("2. Update the URL in this script with your actual GitHub Pages URL")
            print("3. Regenerate the QR code with the correct URL")
            print("4. Share the QR code with your friend!")
            print()
            print("📱 To test: Scan the QR code with your phone's camera")
            print("   (Make sure the webpage is hosted online, not local file://)")
            print()
            print("🎊 Animation Sequence:")
            print("   • 0-5 seconds: Hearts tree formation")
            print("   • 5-7 seconds: Cake slides in")
            print("   • 7-10 seconds: Candles appear and blow out")
            print("   • 10+ seconds: Birthday message with confetti!")
            
        else:
            print("❌ Error: QR code file was not created successfully")
            return False
            
    except ImportError as e:
        print("❌ Error: Required libraries not installed")
        print("Please install the required libraries:")
        print("pip install qrcode[pil]")
        print()
        print("If you're using Python 3, try:")
        print("pip3 install qrcode[pil]")
        return False
        
    except Exception as e:
        print(f"❌ Error generating QR code: {str(e)}")
        return False
    
    return True

def check_dependencies():
    """
    Check if required dependencies are installed.
    """
    try:
        import qrcode
        from PIL import Image
        return True
    except ImportError:
        return False

def main():
    """
    Main function to run the QR code generator.
    """
    print("Checking dependencies...")
    
    if not check_dependencies():
        print("❌ Missing dependencies!")
        print("Installing required packages...")
        print()
        print("Run this command to install dependencies:")
        print("pip install qrcode[pil]")
        print()
        print("Or if you're using Python 3:")
        print("pip3 install qrcode[pil]")
        print()
        print("After installing, run this script again.")
        return
    
    print("✅ Dependencies found!")
    print()
    
    # Generate the QR code
    success = generate_qr_code()
    
    if success:
        print("🎊 QR code generation completed successfully!")
        print("Ready to scan after hosting!")
    else:
        print("💔 QR code generation failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
