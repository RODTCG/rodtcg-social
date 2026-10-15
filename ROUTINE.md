# Instagram draft routine (runs in a fresh session; the owner approves drafts in Metricool)

Goal: keep calendar.md posts ready as Metricool DRAFTS (createScheduledPost with info.draft = true). NEVER schedule/publish directly; the owner approves.

For each post due in the next 2-3 days that is not yet a draft with current numbers:
1. Refresh values first. Listing posts: fetch the eBay listing page (WebFetch, https://www.ebay.com/itm/<ebayItemId>; ids are in https://raw.githubusercontent.com/RODTCG/rod-shop/main/cards.json, which can be stale) and confirm price + still available. If a card sold, skip it, note it, and tell the owner. Market posts: re-check Mew ex FR 158/128 etc. on PriceCharting / Card Codex / Bill's Archive; trackers disagree, so use a range and the date. Not financial advice, observation style.
2. Card photos: the shell cannot download from i.ebayimg.com (403). Use the Batches tracker (https://claude.ai/artifact/HYnnWjA7ETwFFyXtp22gkP): ArtifactData list collection "cards", match name+number, then Artifact read with path = frontId to save the photo. Then crop by the card's outer edge (see CROP table in scripts/build_tags.py; re-measure for new cards).
3. Build images with scripts/build_chart.py / build_tags.py (Pillow, 1080x1350, Inter font). Look at every PNG before using it. No "not financial advice" text on images.
4. Commit PNGs to posts/YYYY-MM/ on main and use https://raw.githubusercontent.com/RODTCG/rodtcg-social/main/posts/YYYY-MM/<file> as media URLs.
5. createScheduledPost: blogId 7417299, providers instagram, instagramData {type POST}, publicationDate 10:00 America/New_York, draft true. A carousel is several media URLs in order. If a draft for that date already exists, use updateScheduledPost (getScheduledPosts to find id) instead of making a duplicate.
6. Update calendar.md and notify the owner which drafts are ready to approve in Metricool, with any sold-out/changed-price notes.
