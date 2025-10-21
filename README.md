# 🎉 Birthday Surprise Webpage & QR Code Generator

A beautiful animated birthday surprise webpage with enhanced animations and QR code generation, inspired by YouTube Shorts! Features hearts tree, cake, candles blow, and confetti effects.

## 📁 Project Structure

```
BirthdaySurprise/
├── index.html          # Main surprise webpage with enhanced animations
├── generate_qr.py      # QR code generator script
├── requirements.txt    # Python dependencies
├── surprise_qr.png     # Generated QR code (after running script)
└── README.md          # This file
```

## 🎨 Enhanced Features

### Webpage (`index.html`)
- **Vibrant Background**: Red-to-blue gradient background (45-degree linear gradient)
- **Hearts Tree Animation**: Canvas-based animation showing hearts forming a tree over 5 seconds
- **Cake Animation**: Birthday cake slides in from bottom after hearts tree completes
- **Candles Blow Animation**: 5 candles appear and blow out with smoke effects (7-10 seconds)
- **Birthday Message**: "Happy Birthday, Dost! 🎉" with bouncing animation
- **Confetti Effect**: Multiple confetti bursts using canvas-confetti library
- **Fullscreen Mode**: Automatically enters fullscreen on page load
- **Mobile Responsive**: Optimized for mobile devices
- **Error Handling**: Fallback cake drawing if image fails to load

### QR Code Generator (`generate_qr.py`)
- Generates QR code linking to the surprise webpage
- Uses `qrcode` and `Pillow` libraries
- Creates `surprise_qr.png` with black fill and white background
- Includes error handling and dependency checking

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install qrcode[pil]
```

Or using the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Test the Webpage Locally

Open `index.html` in your web browser:
- **Windows**: Double-click the file or run `start index.html`
- **Mac**: Double-click the file or run `open index.html`
- **Linux**: Run `xdg-open index.html`

### 3. Set Up GitHub Repository (Automated)

**Windows Users:**
```bash
setup_github.bat
```

**Mac/Linux Users:**
```bash
chmod +x setup_github.sh
./setup_github.sh
```

### 4. Update QR Code with Your URL

After GitHub Pages is set up:
```bash
python update_qr.py YOUR_USERNAME
```

This will create the final `surprise_qr.png` with your actual URL.

## 🌐 Hosting on GitHub Pages

### 🚀 **AUTOMATED SETUP (Recommended)**

**Windows Users:**
```bash
# Run the automated setup script
setup_github.bat
```

**Mac/Linux Users:**
```bash
# Make script executable and run
chmod +x setup_github.sh
./setup_github.sh
```

### 📝 **Manual Setup Steps**

**Step 1: Create GitHub Repository**
1. **Go to [GitHub.com](https://github.com)** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Repository settings:**
   - Name: `BirthdaySurprise`
   - Description: `Birthday surprise webpage with enhanced animations and QR code`
   - Make it **Public** (required for free GitHub Pages)
   - **Don't** initialize with README (we already have files)
5. **Click "Create repository"**

**Step 2: Push Files to GitHub**
```bash
cd BirthdaySurprise
git init
git add .
git commit -m "Initial commit: Birthday surprise project with enhanced animations"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/BirthdaySurprise.git
git push -u origin main
```

**Step 3: Enable GitHub Pages**
1. Go to your repository **Settings** tab
2. Scroll down to **"Pages"** section
3. Under **"Source"**, select **"Deploy from a branch"**
4. Select **"main"** branch and **"/ (root)"** folder
5. Click **"Save"**
6. Wait 5-10 minutes for GitHub Pages to deploy

### Step 4: Get Your URL

Your webpage will be available at:
```
https://YOUR_USERNAME.github.io/BirthdaySurprise/index.html
```

For example: `https://john.github.io/BirthdaySurprise/index.html`

### Step 5: Update QR Code

1. Edit `generate_qr.py`
2. Replace `YOUR_USERNAME` on line 19 with your actual GitHub username:
   ```python
   url = "https://YOUR_USERNAME.github.io/BirthdaySurprise/index.html"
   ```
3. Run the script again:
   ```bash
   python generate_qr.py
   ```

## 📱 Testing Instructions

### Local Testing
1. **Open `index.html` in your browser:**
   - Windows: `start index.html`
   - Mac: `open index.html`
   - Linux: `xdg-open index.html`
2. **The page should automatically go fullscreen**
3. **Watch the enhanced animation sequence:**
   - Hearts tree forms (0-5 seconds)
   - Cake slides in (5-7 seconds)
   - Candles appear and blow out with smoke (7-10 seconds)
   - Message appears with confetti (10+ seconds)

### QR Code Generation Testing
1. **Install dependencies:**
   ```bash
   pip install qrcode[pil]
   ```
2. **Generate QR code:**
   ```bash
   python generate_qr.py
   ```
3. **Verify QR code file:** `surprise_qr.png` should be created

### GitHub Pages Testing
1. **Host your webpage on GitHub Pages** (follow hosting instructions above)
2. **Update QR code with your GitHub Pages URL**
3. **Test the live webpage:** Visit `https://YOUR_USERNAME.github.io/BirthdaySurprise/index.html`
4. **Scan QR code with your phone's camera**
5. **The webpage should open with all enhanced animations**

### Mobile QR Code Testing
1. **Use your phone's camera app** or a QR scanner app
2. **Point camera at the QR code**
3. **Tap the notification** that appears
4. **The webpage should open** with all animations working
5. **Note:** Local `file://` URLs won't work for mobile QR scanning

## 🎯 Enhanced Animation Timeline

- **0-5 seconds**: Hearts tree formation animation
- **5-7 seconds**: Cake slides in from bottom
- **7-10 seconds**: Candles appear and blow out with smoke effects
- **10+ seconds**: Birthday message appears with confetti effects

## 🛠️ Customization

### Change the Message
Edit the text in `index.html`:
```html
<div class="main-message">Happy Birthday, [Name]! 🎉</div>
<div class="sub-message">Your custom message here! ❤️</div>
```

### Change Colors
Modify the gradient in the CSS:
```css
background: linear-gradient(45deg, #your-color-1, #your-color-2);
```

### Change Cake Image
Replace the cake image URL in `index.html`:
```html
<img src="your-cake-image-url.png" alt="Birthday Cake" class="cake-image">
```

### Modify Candles
Adjust the number of candles in the JavaScript:
```javascript
// Create 5 candles (change this number)
for (let i = 0; i < 5; i++) {
```

## 🔧 Troubleshooting

### QR Code Issues
- **"Module not found"**: Run `pip install qrcode[pil]`
- **Unicode errors**: The script now uses ASCII characters for Windows compatibility
- **QR code not working**: Make sure the webpage is hosted online, not local file://

### Webpage Issues
- **Fullscreen not working**: Some browsers block automatic fullscreen
- **Confetti not showing**: Check internet connection for CDN library
- **Cake image not loading**: The page includes a fallback canvas-drawn cake
- **Candles not appearing**: Check browser console for JavaScript errors

### Mobile Issues
- **Page not responsive**: The CSS includes mobile breakpoints
- **Animations too fast/slow**: Adjust timing in JavaScript (milliseconds)

## 📋 Requirements

- **Python 3.6+** for QR code generation
- **Modern web browser** with JavaScript enabled
- **Internet connection** for confetti library (CDN)

## 🎊 Usage Tips

1. **Test locally first** before hosting
2. **Use HTTPS URLs** for QR codes (GitHub Pages provides this)
3. **Share QR code as image** - works on any device with camera
4. **Customize the message** to make it personal
5. **Test on mobile** to ensure responsive design works
6. **Enjoy the enhanced animations** - candles blow with smoke effects!

## 🎉 Enjoy!

Your friend will be amazed when they scan the QR code and see the beautiful animated birthday message with hearts, cake, candles that blow out, and confetti! The enhanced animations create an even more memorable birthday experience.

---

**Note**: This project features enhanced animations including candles that blow out with smoke effects, making it even more engaging than the original YouTube Short inspiration!
