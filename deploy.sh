#!/bin/bash
# Deploy Targeted Design site to Cloudflare Pages
# Usage: ./deploy.sh "optional commit message"

cd /home/nemesis/targeted-design-site

# Stage everything
git add -A

# Commit (use provided message or default)
MSG="${1:-site update}"
git commit -m "$MSG" 2>/dev/null

# Push to git (version control)
git push origin main 2>/dev/null

# Deploy to Cloudflare Pages
npx wrangler pages deploy . --project-name targeted-design --commit-dirty=true

echo ""
echo "✓ Deployed. Verify at https://targeted-design.com"
