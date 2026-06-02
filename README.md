# CRBC Contacts GitHub Pages Demo

This folder is a static GitHub Pages contact-card demo.

## Files

- `index.html`: contact list page
- `c/yi-wenwen/index.html`: Yi Wenwen / Allison Yi contact page
- `contacts/yi-wenwen-cn.vcf`: Chinese contact card
- `contacts/allison-yi-en.vcf`: English contact card
- `qr/yi-wenwen-page.png`: QR code for the contact page
- `qr/yi-wenwen-page.svg`: print-ready QR code for the contact page

## Free GitHub Pages Setup

1. Create a public GitHub repository named `crbc-contacts`.
2. Upload all files in this folder to the repository root.
3. Open repository `Settings`.
4. Go to `Pages`.
5. Under `Build and deployment`, choose `Deploy from a branch`.
6. Select branch `main` and folder `/root`.
7. Save.

After GitHub publishes the site, the URL will be:

```text
https://YOUR_GITHUB_USERNAME.github.io/crbc-contacts/
```

The Yi Wenwen contact page will be:

```text
https://YOUR_GITHUB_USERNAME.github.io/crbc-contacts/c/yi-wenwen/
```

Replace `YOUR_GITHUB_USERNAME` in `generate_qr.py`, then run it again to generate final QR codes.
