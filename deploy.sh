#!/bin/bash
# Deploy Targeted Design site to Cloudflare Pages
# Usage: ./deploy.sh "optional commit message"

cd /home/nemesis/targeted-design-site

# Stage everything
git add -A

# Commit (use provided message or default)
MSG="${1:-site update}"
git commit -m "$MSG"

# Push to git (version control)
git push origin main

# Deploy to Cloudflare Pages (this is what actually goes live)
npx wrangler pages deploy . --project-name targeted-design

echo ""
echo "✓ Deployed. Verify at https://targeted-design.com"