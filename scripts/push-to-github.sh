#!/bin/bash
set -e

echo "🔧 Preparing to push to GitHub..."
git init
git add .
git commit -m "Initial commit: Locallhost.dev setup"
git branch -M main
git remote add origin https://github.com/Web4application/locallhost-dev-guide.git
git push -u origin main
echo "✅ Successfully pushed to GitHub: locallhost-dev-guide"
