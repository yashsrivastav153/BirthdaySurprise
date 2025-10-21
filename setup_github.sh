#!/bin/bash
echo "🎉 Setting up GitHub repository for Birthday Surprise! 🎉"
echo

read -p "Enter your GitHub username: " USERNAME
echo

echo "Step 1: Initialize Git repository"
git init

echo "Step 2: Add all files"
git add .

echo "Step 3: Create initial commit"
git commit -m "Initial commit: Birthday surprise webpage with enhanced animations"

echo "Step 4: Set main branch"
git branch -M main

echo "Step 5: Add remote origin"
git remote add origin https://github.com/$USERNAME/BirthdaySurprise.git

echo "Step 6: Push to GitHub"
git push -u origin main

echo
echo "✅ Files pushed to GitHub successfully!"
echo
echo "📝 Final Steps:"
echo "1. Go to https://github.com/$USERNAME/BirthdaySurprise"
echo "2. Go to Settings > Pages > Enable GitHub Pages (main branch, root folder)"
echo "3. Wait 5-10 minutes for deployment"
echo "4. Run: python update_qr.py $USERNAME"
echo
echo "🎊 Your surprise will be ready at: https://$USERNAME.github.io/BirthdaySurprise/index.html"
