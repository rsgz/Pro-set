import requests
# from settings import authorization

import requests

authorization="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiIxIiwiVXNlckFjY291bnRJZCI6IjEiLCJOaWNrbmFtZSI6IueUsOS8r-WFiSIsIlJvbGUiOiJhZG1pbiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJhZG1pbiIsImV4cCI6MTc0Mjk3MjE2NCwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MjAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MjAwIn0.t0cvirxC5J54CloQbT-Tnubbx8RhfYGW_vPdBUSoq6c"

# 添加后缀  批量加100个后缀 随机和标题进行组合
def add_houzhui(websiteId=793, classificationId='2251937252638720', newValue=''):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'action-name': 'shop-goods.update.batch',
        'authorization': authorization,
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://b08-admin.shop6888.com',
        'priority': 'u=1, i',
        'referer': 'https://b08-admin.shop6888.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'options': {
            'classificationId': classificationId,
            'searchHierarchyMethod': 3,
            'websiteId': websiteId,
        },
        'updateColumns': [
            {
                'name': 'title',
                'operator': 2,
                # 'newValue': 'Hoodie Sweatshirt Pullover\nZip Hoodie Drawstring Kangaroo Pocket\nCotton Hoodie Fleece Lining Warmth\nOversized Hoodie Comfort Casual\nGraphic Hoodie Design Print\nHooded Sweatshirt Casual Wear Street Style\nHoodie Jacket Zipper Layering\nHoodie Dress Longline Feminine\nHoodie Crop Top Short Trendy\nHoodie with Logo Branding Identity\nHoodie with Pocket Utility Practical\nHoodie with Hood Adjustable Protection\nHoodie with Strings Custom Fit Adjustable\nHoodie with Print Artistic Unique\nHoodie with Embroidery Detailed Premium\nHoodie with Patch Decorative Personalized\nHoodie with Ribbed Cuffs Snug Fit Comfort\nHoodie with Ribbed Hem Stretchable Secure\nHoodie with Thumb Holes Functional Cozy\nHoodie with Zipper Versatile Modern\nHoodie with Button Classic Timeless\nHoodie with Drawcord Adjustable Secure\nHoodie with Lining Warm Insulated\nHoodie with Fur Luxurious Winter\nHoodie with Pattern Geometric Abstract\nHoodie with Stripes Bold Sporty\nHoodie with Color Block Contrast Stylish\nHoodie with Typography Text Message\nHoodie with Illustration Artistic Creative\nHoodie with Emblem Brand Identity\nHoodie with Applique Textured Unique\nHoodie with Sequins Glamorous Eye-catching\nHoodie with Rhinestones Sparkly Elegant\nHoodie with Lace Feminine Delicate\nHoodie with Mesh Breathable Sporty\nHoodie with Reflective Safety Nightwear\nHoodie with Camouflage Military Edgy\nHoodie with Tie-Dye Psychedelic Retro\nHoodie with Gradient Ombre Colorful\nHoodie with Metallic Shiny Futuristic\nHoodie with Neon Bright Vibrant\nHoodie with Pastel Soft Subtle\nHoodie with Earth Tones Natural Calm\nHoodie with Monochrome Minimalist Simple\nHoodie with Contrast Stitching Detailed Premium\nHoodie with Raw Hem Edgy Unfinished\nHoodie with Distressed Vintage Worn\nHoodie with Frayed Bohemian Relaxed\nHoodie with Oversized Fit Loose Comfortable\nHoodie with Slim Fit Tailored Modern\nHoodie with Relaxed Fit Easy Casual\nHoodie with Cropped Fit Short Trendy\nHoodie with Longline Fit Extended Stylish\nHoodie with Drop Shoulder Relaxed Streetwear\nHoodie with Raglan Sleeves Sporty Comfortable\nHoodie with Set-In Sleeves Structured Classic\nHoodie with Batwing Sleeves Loose Dramatic\nHoodie with Bell Sleeves Flared Feminine\nHoodie with Puffed Sleeves Voluminous Trendy\nHoodie with Rolled Sleeves Casual Relaxed\nHoodie with Cuffed Sleeves Snug Secure\nHoodie with Elastic Cuffs Stretchable Comfortable\nHoodie with Ribbed Neckline Snug Warm\nHoodie with V-Neck Classic Versatile\nHoodie with Crew Neck Simple Timeless\nHoodie with High Neck Warm Protective\nHoodie with Mock Neck Collared Structured\nHoodie with Turtle Neck Cozy Winter\nHoodie with Button Placket Classic Preppy\nHoodie with Zipper Placket Modern Functional\nHoodie with Hidden Zipper Minimalist Clean\nHoodie with Exposed Zipper Edgy Industrial\nHoodie with Double Zipper Versatile Adjustable\nHoodie with Half-Zip Sporty Casual\nHoodie with Full-Zip Functional Layering\nHoodie with Snap Buttons Easy Quick\nHoodie with Toggle Buttons Decorative Unique\nHoodie with Magnetic Closure Innovative Modern\nHoodie with Velcro Closure Adjustable Secure\nHoodie with Drawstring Waist Adjustable Fitted\nHoodie with Elastic Waist Stretchable Comfortable\nHoodie with Belted Waist Structured Tailored\nHoodie with Tied Waist Feminine Flattering\nHoodie with High-Low Hem Asymmetrical Trendy\nHoodie with Slit Hem Functional Movement\nHoodie with Side Slits Relaxed Casual\nHoodie with Front Slit Layering Stylish\nHoodie with Back Slit Movement Comfort\nHoodie with Hem Detail Decorative Unique\nHoodie with Hem Ribbing Snug Secure\nHoodie with Hem Elastic Stretchable Comfortable\nHoodie with Hem Drawcord Adjustable Customizable\nHoodie with Hem Fringe Bohemian Relaxed\nHoodie with Hem Lace Feminine Delicate\nHoodie with Hem Embroidery Detailed Premium\nHoodie with Hem Applique Textured Unique\nHoodie with Hem Patch Decorative Personalized\nHoodie with Hem Contrast Bold Stylish\nHoodie with Hem Raw Edge Edgy Unfinished\nHoodie with Hem Frayed Vintage Worn',
                'newValue': newValue,
            },
        ],
        "updateDetailColumns": []
    }

    response = requests.post('https://b03-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print(response,websiteId,classificationId)

Blazers_l=r"""
 Women's Blazers
 Slim Fit Blazers
 Tailored Blazers
 Casual Blazers
 Formal Blazers
 Double-Breasted Blazers
 Single-Breasted Blazers
 Velvet Blazers
 Linen Blazers
 Wool Blazers
 Silk Blazers
 Embroidered Blazers
 Patterned Blazers
 Solid Color Blazers
 Checked Blazers
 Striped Blazers
 Floral Blazers
 Vintage Blazers
 Modern Blazers
 Cropped Blazers
 Longline Blazers
 Belted Blazers
 Buttoned Blazers
 Zippered Blazers
 High-Neck Blazers
 V-Neck Blazers
 Lapel Blazers
 Collared Blazers
 Sleeveless Blazers
 Lightweight Blazers
 Heavyweight Blazers
 Quilted Blazers
 Padded Blazers
 Fitted Blazers
 Oversized Blazers
 Stretch Blazers
 Elastic Blazers
 Adjustable Blazers
 Reversible Blazers
 Metallic Blazers
 Shimmer Blazers
 Matte Blazers
 Textured Blazers
 Sheer Blazers
 Mesh Blazers
 Lace Blazers
 Crochet Blazers
 Knitted Blazers
 Woven Blazers
 Denim Blazers
 Leather Blazers
 Faux Fur Blazers
 Hooded Blazers
 Pocketed Blazers
 Buttonless Blazers
 Asymmetrical Blazers
 Layered Blazers
 Tiered Blazers
 Ruffled Blazers
 Pleated Blazers
 Draped Blazers
 Belted Back Blazers
 Side-Tie Blazers
 Front-Tie Blazers
 Backless Blazers
 Cut-Out Blazers
 High-Slit Blazers
 Low-Back Blazers
 Open-Front Blazers
 Closed-Front Blazers
 Wrap Blazers
 Peplum Blazers
 Tunic Blazers
 Cropped Vest Blazers
 Long Vest Blazers
 Blazer Dresses
 Blazer Jackets
 Blazer Coats
 Blazer Cardigans
 Blazer Sweaters
 Blazer Tops
 Blazer Shirts
 Blazer Tunics
 Blazer Overcoats
 Blazer Ponchos
 Blazer Capes
 Blazer Kimonos
 Blazer Blouses
 Blazer Bodysuits
 Blazer Jumpsuits
 Blazer Rompers
 Blazer Skirts
 Blazer Pants
 Blazer Shorts
 Blazer Leggings
 Blazer Joggers
 Blazer Hoodies
 Blazer Sweatshirts
 Blazer T-Shirts
 Blazer Tank Tops
 Blazer Camisoles
 Blazer Bralettes
 Blazer Corsets
 Blazer Bustiers
 Blazer Gilets
 Blazer Vests
 Blazer Sleeves
 Blazer Armholes
 Blazer Hemlines
 Blazer Necklines
 Blazer Silhouettes
 Blazer Fabrics
 Blazer Patterns
 Blazer Designs
 Blazer Styles
 Blazer Trends
 Blazer Collections
 Blazer Outfits
 Blazer Ensembles
 Blazer Accessories
 Blazer Belts
 Blazer Buttons
 Blazer Zippers
 Blazer Snaps
 Blazer Hooks
 Blazer Loops
 Blazer Ties
 Blazer Straps
 Blazer Buckles
 Blazer Chains
 Blazer Charms
 Blazer Embellishments
 Blazer Appliques
 Blazer Patches
 Blazer Embroidery
 Blazer Beading
 Blazer Sequins
 Blazer Rhinestones
 Blazer Pearls
 Blazer Crystals
 Blazer Gems
 Blazer Stones
 Blazer Metals
 Blazer Leathers
 Blazer Suedes
 Blazer Furs
 Blazer Linings
 Blazer Interiors
 Blazer Exteriors
 Blazer Details
"""

Blouses_Shirts_l=r"""
 Women's Blouses
 Silk Shirts
 Button-Down Shirts
 Lace Tops
 Floral Blouses
 Ruffled Shirts
 Sleeveless Blouses
 Striped Shirts
 Peplum Tops
 Chiffon Blouses
 Off-Shoulder Tops
 Printed Shirts
 Wrap Blouses
 Long-Sleeve Shirts
 Embroidered Tops
 V-Neck Blouses
 Casual Shirts
 Sheer Blouses
 Bow Tie Tops
 Denim Shirts
 High-Neck Blouses
 Cropped Shirts
 Satin Blouses
 Plaid Shirts
 Puff Sleeve Tops
 Tie-Front Blouses
 Linen Shirts
 Cold-Shoulder Tops
 Geometric Print Blouses
 Tunic Shirts
 Mesh Tops
 Flutter Sleeve Blouses
 Solid Color Shirts
 Halter Neck Tops
 Belted Blouses
 Oversized Shirts
 Sequin Tops
 Boho Blouses
 Crochet Shirts
 Asymmetrical Tops
 Polka Dot Blouses
 Fitted Shirts
 Metallic Tops
 Layered Blouses
 Relaxed Fit Shirts
 Tassel Tops
 Vintage Blouses
 Cropped Blouses
 Tropical Print Shirts
 Smocked Tops
 High-Low Blouses
 Button-Front Shirts
 Glitter Tops
 Tiered Blouses
 Casual Blouses
 Lace-Up Shirts
 Ruffled Sleeve Tops
 Flowy Blouses
 Striped Blouses
 Collared Shirts
 Sheer Sleeve Tops
 Belted Shirts
 Embellished Blouses
 Longline Shirts
 Cut-Out Tops
 Floral Print Blouses
 Relaxed Blouses
 Fringe Tops
 Wrap Shirts
 High-Neck Tops
 Cropped Button-Downs
 Chiffon Shirts
 Peplum Blouses
 Sleeveless Shirts
 Printed Blouses
 Off-Shoulder Blouses
 Lace Blouses
 Denim Tops
 Silk Tops
 Ruffled Blouses
 Button-Up Shirts
 Flowy Shirts
 Embroidered Blouses
 V-Neck Shirts
 Casual Tops
 Sheer Shirts
 Bow Tie Blouses
 Long-Sleeve Blouses
 Striped Tops
 Satin Shirts
 Plaid Blouses
 Puff Sleeve Blouses
 Tie-Front Shirts
 Linen Blouses
 Cold-Shoulder Blouses
 Geometric Print Shirts
 Tunic Blouses
 Mesh Blouses
 Flutter Sleeve Shirts
 Solid Color Blouses
 Halter Neck Blouses
 Belted Tops
 Oversized Blouses
 Sequin Blouses
 Boho Shirts
 Crochet Blouses
 Asymmetrical Blouses
 Polka Dot Shirts
 Fitted Blouses
 Metallic Blouses
 Layered Shirts
 Relaxed Fit Blouses
 Tassel Blouses
 Vintage Shirts
 Cropped Tops
 Tropical Print Blouses
 Smocked Blouses
 High-Low Shirts
 Button-Front Blouses
 Glitter Blouses
 Tiered Shirts
 Lace-Up Blouses
 Ruffled Sleeve Blouses
 Flowy Tops
 Collared Blouses
 Sheer Sleeve Blouses
 Embellished Shirts
 Longline Blouses
 Cut-Out Blouses
 Floral Print Shirts
 Relaxed Tops
 Fringe Blouses
 Wrap Tops
 High-Neck Shirts
 Cropped Button-Ups
 Chiffon Tops
 Peplum Shirts
 Printed Tops
 Off-Shoulder Shirts
 Denim Blouses
 Silk Blouses
 Ruffled Tops
 Button-Up Blouses
 Embroidered Shirts
"""

Bottoms_l=r"""
 Women's Shorts
 High-Waisted Pants
 Skinny Jeans
 Wide-Leg Trousers
 Denim Skirts
 Casual Leggings
 Paperbag Waist Pants
 Cropped Jeans
 Cargo Pants
 Pleated Skirts
 Tailored Trousers
 Jogger Pants
 Leather Leggings
 Flared Jeans
 Midi Skirts
 Culottes
 Mom Jeans
 Bermuda Shorts
 Linen Pants
 Maxi Skirts
 Harem Pants
 Denim Shorts
 Palazzo Pants
 A-Line Skirts
 Stretch Jeans
 Track Pants
 Velvet Leggings
 Bootcut Jeans
 Pencil Skirts
 Drawstring Pants
 Distressed Jeans
 Chino Shorts
 Tapered Trousers
 Tiered Skirts
 Corduroy Pants
 High-Slit Skirts
 Straight-Leg Jeans
 Lounge Pants
 Sequin Skirts
 Elastic Waist Pants
 Boyfriend Jeans
 Biker Shorts
 Wrap Skirts
 Wide-Belt Pants
 Ripped Jeans
 Yoga Pants
 Pleated Pants
 Mini Skirts
 Relaxed Fit Jeans
 Lace Trim Skirts
 Cuffed Pants
 Low-Rise Jeans
 Athletic Shorts
 Layered Skirts
 Belted Trousers
 Frayed Jeans
 Knit Pants
 Asymmetrical Skirts
 Slim Fit Jeans
 High-Rise Shorts
 Draped Pants
 Denim Overalls
 Ruffled Skirts
 Cropped Trousers
 Acid Wash Jeans
 Cycling Shorts
 Gathered Skirts
 Side-Stripe Pants
 Vintage Jeans
 Lace-Up Skirts
 Elastic Cuff Pants
 Patchwork Jeans
 Running Shorts
 Sheer Skirts
 Button-Fly Jeans
 Wide-Cuff Pants
 Boho Skirts
 Stretch Waist Pants
 Stonewash Jeans
 Tennis Skirts
 High-Slit Pants
 Distressed Shorts
 Tulle Skirts
 Slim Leg Pants
 Raw Hem Jeans
 Gym Shorts
 Wrap Pants
 Denim Jumpsuits
 Tiered Pants
 Metallic Skirts
 Relaxed Waist Jeans
 Cargo Shorts
 Layered Pants
 Sequin Pants
 High-Waist Shorts
 Pleated Culottes
 Faux Leather Skirts
 Straight Fit Jeans
 Drawstring Shorts
 Flowy Pants
 Embroidered Jeans
 Skater Skirts
 Wide-Leg Jeans
 Lace Pants
 Denim Capris
 Belted Shorts
 Draped Skirts
 Slim Fit Pants
 Ripped Shorts
 Taffeta Skirts
 High-Rise Jeans
 Cargo Joggers
 Mesh Skirts
 Cropped Culottes
 Distressed Denim
 Running Pants
 Satin Skirts
 Relaxed Fit Pants
 Frayed Shorts
 Tiered Culottes
 Stretch Fit Jeans
 Lace-Up Pants
 Denim Skorts
 High-Waist Culottes
 Pleated Shorts
 Sheer Pants
 Vintage Shorts
 Flared Skirts
 Slim Fit Culottes
 Cuffed Jeans
 Athletic Pants
 Ruffled Pants
 Low-Rise Shorts
 Layered Culottes
 Stretch Shorts
 Draped Culottes
 High-Slit Shorts
 Tapered Jeans
 Knit Skirts
 Relaxed Culottes
 Cropped Shorts
 Asymmetrical Pants
 Faux Leather Pants
 High-Rise Culottes
 Flowy Culottes
 Embroidered Pants
 Denim Bermudas
 Tiered Shorts
 Wide-Leg Culottes
"""

Coats_l=r"""
 Women's Coats
 Wool Coats
 Winter Coats
 Puffer Coats
 Down Coats
 Parka Coats
 Trench Coats
 Pea Coats
 Duffle Coats
 Faux Fur Coats
 Leather Coats
 Denim Coats
 Quilted Coats
 Fleece Coats
 Hooded Coats
 Belted Coats
 Zippered Coats
 Buttoned Coats
 Double-Breasted Coats
 Single-Breasted Coats
 Military Coats
 Biker Coats
 Motorcycle Coats
 Aviator Coats
 Cape Coats
 Poncho Coats
 Kimono Coats
 Wrap Coats
 Shacket Coats
 Shearling Coats
 Padded Coats
 Lightweight Coats
 Heavyweight Coats
 Waterproof Coats
 Insulated Coats
 Reversible Coats
 Metallic Coats
 Shimmer Coats
 Matte Coats
 Textured Coats
 Sheer Coats
 Mesh Coats
 Lace Coats
 Crochet Coats
 Knitted Coats
 Woven Coats
 Quilted Jackets
 Puffer Jackets
 Down Jackets
 Ski Jackets
 Snow Jackets
 Winter Jackets
 Spring Jackets
 Summer Jackets
 Fall Jackets
 Seasonal Jackets
 Casual Jackets
 Formal Jackets
 Party Jackets
 Evening Jackets
 Work Jackets
 Outdoor Jackets
 Hiking Jackets
 Travel Jackets
 Fashion Jackets
 Trendy Jackets
 Vintage Jackets
 Modern Jackets
 Classic Jackets
 Contemporary Jackets
 Designer Jackets
 High-Street Jackets
 Budget Jackets
 Luxury Jackets
 Embroidered Jackets
 Patterned Jackets
 Solid Color Jackets
 Checked Jackets
 Striped Jackets
 Floral Jackets
 Animal Print Jackets
 Geometric Jackets
 Abstract Jackets
 Graphic Jackets
 Printed Jackets
 Embellished Jackets
 Beaded Jackets
 Sequined Jackets
 Rhinestone Jackets
 Pearl Jackets
 Crystal Jackets
 Gem Jackets
 Stone Jackets
 Metal Jackets
 Leather Trim Jackets
 Faux Fur Trim Jackets
 Shearling Trim Jackets
 Wool Blend Coat
 Longline Trench Coat
 Faux Fur Coat
 Double-Breasted Peacoat
 Quilted Puffer Coat
 Belted Trench Coat
 Oversized Wool Coat
 Waterproof Raincoat
 Shearling Lined Coat
 Hooded Parka Coat
 Cashmere Overcoat
 Fitted Toggle Coat
 Lightweight Spring Coat
 Military Style Coat
 Cropped Puffer Jacket
 Velvet Trim Coat
 Hooded Trench Coat
 Faux Leather Coat
 Wrap Style Coat
 Quilted Hooded Coat
 Longline Peacoat
 Faux Shearling Coat
 Belted Wool Coat
 Water-Repellent Parka
 Oversized Trench Coat
 Faux Fur Trim Coat
 Double-Faced Wool Coat
 Hooded Puffer Coat
 Tailored Overcoat
 Lightweight Raincoat
 Military Peacoat
 Cropped Wool Coat
 Velvet Collar Coat
 Hooded Faux Fur Coat
 Fitted Wrap Coat
 Quilted Longline Coat
 Longline Cashmere Coat
 Faux Shearling Jacket
 Belted Toggle Coat
 Waterproof Trench Coat
 Oversized Faux Fur Coat
 Double-Breasted Overcoat
 Hooded Quilted Coat
 Tailored Peacoat
 Lightweight Parka
 Military Style Trench
 Cropped Faux Fur Coat
 Velvet Lined Coat
 Hooded Wool Coat
 Fitted Puffer Coat
 Quilted Wrap Coat
 Longline Faux Fur Coat
 Faux Shearling Overcoat
 Belted Raincoat
 Water-Repellent Trench
 Oversized Peacoat
 Double-Faced Cashmere Coat
 Hooded Double-Breasted Coat
 Tailored Trench Coat
 Lightweight Quilted Coat
 Military Parka
 Cropped Toggle Coat
 Velvet Trim Peacoat
 Hooded Faux Shearling Coat
 Fitted Longline Coat
 Quilted Faux Fur Coat
 Longline Wool Overcoat
 Faux Shearling Trench
 Belted Puffer Coat
 Waterproof Parka
 Oversized Toggle Coat
 Double-Breasted Trench
 Hooded Cashmere Coat
 Tailored Faux Fur Coat
 Lightweight Faux Shearling Coat
 Military Style Overcoat
 Cropped Quilted Coat
 Velvet Collar Trench
 Hooded Wrap Coat
 Fitted Peacoat
 Quilted Military Coat
 Longline Faux Shearling Coat
 Faux Fur Lined Coat
 Belted Wool Overcoat
 Water-Repellent Peacoat
 Oversized Quilted Coat
 Double-Faced Trench Coat
 Hooded Lightweight Coat
 Tailored Parka
 Lightweight Double-Breasted Coat
 Military Toggle Coat
 Cropped Velvet Coat
 Hooded Faux Leather Coat
 Fitted Trench Coat
 Quilted Oversized Coat
 Longline Military Coat
 Faux Shearling Peacoat
 Belted Faux Fur Coat
 Waterproof Overcoat
 Oversized Faux Shearling Coat
 Double-Breasted Parka
 Hooded Tailored Coat
 Lightweight Quilted Jacket
 Military Style Faux Fur Coat
 Cropped Cashmere Coat
 Velvet Trim Overcoat
 Hooded Wrap Style Coat
 Fitted Quilted Coat
 Quilted Faux Shearling Coat
 Longline Waterproof Coat
 Faux Fur Collar Coat
 Belted Trench Style Coat
 Oversized Military Coat
 Double-Faced Peacoat
 Hooded Lightweight Parka
 Tailored Faux Shearling Coat
 Lightweight Toggle Coat
 Military Quilted Coat
 Cropped Velvet Trim Coat
 Hooded Double-Faced Coat
 Fitted Longline Trench
 Quilted Oversized Parka
 Longline Faux Leather Coat
 Faux Shearling Toggle Coat
 Belted Waterproof Coat
 Oversized Tailored Coat
 Double-Breasted Quilted Coat
 Hooded Cashmere Overcoat
 Lightweight Faux Fur Coat
 Military Style Wrap Coat
 Cropped Faux Shearling Coat
 Velvet Lined Trench
 Hooded Quilted Peacoat
 Fitted Double-Breasted Coat
 Quilted Lightweight Coat
 Longline Military Style Coat
 Faux Fur Trim Overcoat
 Belted Faux Shearling Coat
 Water-Repellent Faux Fur Coat
 Oversized Quilted Trench
 Double-Faced Parka
 Hooded Tailored Overcoat
 Lightweight Velvet Coat
 Military Faux Shearling Coat
 Cropped Waterproof Coat
 Hooded Double-Breasted Trench
 Fitted Quilted Parka
 Quilted Faux Leather Coat
 Longline Lightweight Coat
 Faux Shearling Wrap Coat
"""

Leggings_l=r"""
 Women's Leggings
 High-Waisted Leggings
 Casual Leggings
 Formal Leggings
 Party Leggings
 Evening Leggings
 Work Leggings
 Outdoor Leggings
 Hiking Leggings
 Travel Leggings
 Fashion Leggings
 Trendy Leggings
 Vintage Leggings
 Modern Leggings
 Classic Leggings
 Contemporary Leggings
 Designer Leggings
 High-Street Leggings
 Budget Leggings
 Luxury Leggings
 Embroidered Leggings
 Patterned Leggings
 Solid Color Leggings
 Checked Leggings
 Striped Leggings
 Floral Leggings
 Animal Print Leggings
 Geometric Leggings
 Abstract Leggings
 Graphic Leggings
 Printed Leggings
 Embellished Leggings
 Beaded Leggings
 Sequined Leggings
 Rhinestone Leggings
 Pearl Leggings
 Crystal Leggings
 Gem Leggings
 Stone Leggings
 Metal Leggings
 Leather Trim Leggings
 Faux Fur Trim Leggings
 Shearling Trim Leggings
 Hooded Leggings
 Belted Leggings
 Zippered Leggings
 Buttoned Leggings
 Double-Breasted Leggings
 Single-Breasted Leggings
 Military Leggings
 Biker Leggings
 Motorcycle Leggings
 Aviator Leggings
 Cape Leggings
 Poncho Leggings
 Kimono Leggings
 Wrap Leggings
 Shacket Leggings
 Shearling Leggings
 Padded Leggings
 Lightweight Leggings
 Heavyweight Leggings
 Waterproof Leggings
 Insulated Leggings
 Reversible Leggings
 Metallic Leggings
 Shimmer Leggings
 Matte Leggings
 Textured Leggings
 Sheer Leggings
 Mesh Leggings
 Lace Leggings
 Crochet Leggings
 Knitted Leggings
 Woven Leggings
 Quilted Leggings
 Puffer Leggings
 Down Leggings
 Ski Leggings
 Snow Leggings
 Winter Leggings
 Spring Leggings
 Summer Leggings
 Fall Leggings
 Seasonal Leggings
 Seamless Yoga Leggings
 Compression Workout Leggings
 Mesh Panel Leggings
 Printed Athletic Leggings
 Faux Leather Leggings
 High-Rise Leggings
 Stretch Cotton Leggings
 Side Striped Leggings
 Cropped Leggings
 Thermal Fleece Leggings
 Lace Trim Leggings
 Pocketed Running Leggings
 Ribbed Knit Leggings
 High-Waist Tummy Control
 Sheer Insert Leggings
 Wide Waistband Leggings
 Reflective Detail Leggings
 Longline Leggings
 Fold-Over Waist Leggings
 Metallic Finish Leggings
 Tie-Dye Print Leggings
 Scrunch Butt Leggings
 Lightweight Running Leggings
 High-Compression Leggings
 Side Pocket Leggings
 Floral Print Leggings
 Cropped Yoga Leggings
 Faux Suede Leggings
 High-Rise Compression Leggings
 Seamless Running Leggings
 Mesh Cutout Leggings
 Printed Capri Leggings
 Tummy Control Leggings
 Lace-Up Detail Leggings
 Ribbed High-Waist Leggings
 Thermal Running Leggings
 Side Sheer Leggings
 Wide Elastic Waistband
 Reflective Striped Leggings
 Longline Yoga Leggings
 Fold-Over Compression Leggings
 Metallic Thread Leggings
 Tie-Dye Yoga Leggings
 Scrunch Detail Leggings
 Lightweight Capri Leggings
 High-Compression Running Leggings
 Side Zip Pocket Leggings
 Floral Yoga Leggings
 Cropped Faux Leather Leggings
 High-Rise Tummy Control
 Seamless Workout Leggings
 Mesh Panel Yoga Leggings
 Printed High-Waist Leggings
 Tummy Slimming Leggings
 Lace Back Leggings
 Ribbed Compression Leggings
 Thermal Yoga Leggings
 Side Sheer Panel Leggings
 Embroidered Yoga Leggings
 Wide Waistband Running Leggings
 Reflective Print Leggings
 Longline Compression Leggings
 Fold-Over Yoga Leggings
 Metallic Sheen Leggings
 Tie-Dye Running Leggings
 Scrunch Butt Yoga Leggings
 Lightweight High-Waist Leggings
 High-Compression Capri Leggings
 Side Pocket Yoga Leggings
 Floral Print Running Leggings
 Cropped Seamless Leggings
 Faux Leather Yoga Leggings
 High-Rise Mesh Leggings
 Seamless Tummy Control Leggings
 Mesh Insert Running Leggings
 Printed Scrunch Leggings
 Tummy Shaping Leggings
 Lace Detail Yoga Leggings
 Ribbed High-Compression Leggings
 Thermal High-Waist Leggings
 Side Sheer Yoga Leggings
 Embellished Running Leggings
 Wide Waistband Yoga Leggings
 Reflective Yoga Leggings
 Longline Tummy Control Leggings
 Fold-Over Running Leggings
 Metallic Print Leggings
 Tie-Dye High-Waist Leggings
 Scrunch Detail Running Leggings
 Lightweight Seamless Leggings
 High-Compression Yoga Leggings
 Side Zip Yoga Leggings
 Floral Print Capri Leggings
 Cropped Compression Leggings
 Faux Leather Running Leggings
 High-Rise Scrunch Leggings
 Seamless Mesh Leggings
 Printed Tummy Control Leggings
 Tummy Slimming Yoga Leggings
 Lace-Up Yoga Leggings
 Ribbed Running Leggings
 Thermal Compression Leggings
 Side Sheer Running Leggings
 Embroidered Running Leggings
 Wide Waistband Capri Leggings
 Reflective High-Waist Leggings
 Longline Yoga Capri Leggings
 Fold-Over Tummy Control Leggings
 Metallic Running Leggings
 Tie-Dye Scrunch Leggings
 Scrunch Butt Running Leggings
 Lightweight Mesh Leggings
 High-Compression Seamless Leggings
 Side Pocket Running Leggings
 Floral Print High-Waist Leggings
 Cropped Mesh Leggings
 Faux Leather Tummy Control Leggings
 High-Rise Printed Leggings
 Seamless Scrunch Leggings
 Mesh Panel Running Leggings
 Printed Yoga Capri Leggings
 Tummy Shaping Running Leggings
 Lace Detail Running Leggings
 Ribbed Tummy Control Leggings
 Thermal Yoga Capri Leggings
 Side Sheer Capri Leggings
 Embellished Yoga Leggings
 Wide Waistband Running Capri
 Reflective Scrunch Leggings
 Longline Running Leggings
 Fold-Over Yoga Capri Leggings
 Metallic Tummy Control Leggings
 Tie-Dye Mesh Leggings
 Scrunch Detail Capri Leggings
 Lightweight High-Compression Leggings
 High-Compression Mesh Leggings
 Side Zip Running Leggings
 Floral Print Scrunch Leggings
 Cropped Tummy Control Leggings
 Faux Leather Yoga Capri Leggings
 High-Rise Seamless Leggings
 Seamless Running Capri Leggings
 Mesh Insert Yoga Leggings
 Printed High-Compression Leggings
 Tummy Slimming Running Leggings
 Lace-Up Running Leggings
 Ribbed Yoga Capri Leggings
"""

Outerwear_l=r"""
 Women's Swimwear
 Stylish Swimsuits
 Trendy Bikini Sets
 One-Piece Swimsuit
 Beachwear Collection
 Summer Swimwear
 Sexy Bikini Tops
 High-Waisted Bottoms
 Floral Swimsuits
 Striped Bikini Sets
 Halter Neck Swimwear
 Push-Up Bikini
 Tankini Outfits
 Sheer Cover-Ups
 Crochet Bikini
 Ruffled Swimsuits
 Mesh Swimwear
 Cut-Out Designs
 Strapless Bikini
 Printed Swimsuits
 Vintage Swimwear
 Sporty Bikini
 Lace-Up Swimsuits
 Tropical Prints
 High-Cut Bottoms
 Plunge Neckline
 Bandeau Bikini
 Tied Swimsuits
 Bold Color Swimwear
 Geometric Patterns
 Longline Tops
 Cheeky Bottoms
 Off-Shoulder Swimwear
 Metallic Swimsuits
 Animal Print Bikini
 Cropped Swim Top
 Side-Tie Bottoms
 Boho Swimsuits
 Glitter Swimwear
 Underwire Bikini
 Retro Swimsuits
 Solid Color Swimwear
 Embroidered Bikini
 Ruffle Bikini Tops
 Mesh Panel Swimsuits
 High-Neck Swimwear
 Low-Back Swimsuits
 Two-Tone Bikini
 Adjustable Swimwear
 Tassel Bikini Sets
 Pastel Swimsuits
 Neon Swimwear
 Shimmer Bikini
 Lace Trim Swimsuits
 Belted One-Piece
 Triangle Bikini
 Wrap Swimwear
 Crochet Cover-Ups
 Strappy Swimsuits
 Textured Swimwear
 Seamless Bikini
 Reversible Swimsuits
 Halter Bikini Tops
 Side-Cut Swimwear
 Fringed Bikini
 Sheer Panel Swimsuits
 Bold Print Swimwear
 Crisscross Bikini
 Cutout One-Piece
 Tied Halter Swimsuits
 Metallic Sheen Swimwear
 High-Leg Swimsuits
 Ruffled One-Piece
 Tropical Bikini
 Lace-Up Bikini
 Sporty One-Piece
 Floral Print Swimwear
 Deep V-Neck Swimsuits
 Color Block Bikini
 Cropped Swim Cover
 Strappy One-Piece
 Sheer Swim Cover
 Bold Striped Swimwear
 Cutout Bikini Tops
 High-Waist Swimsuits
 Mesh Insert Swimwear
 Tassel Trim Bikini
 Retro One-Piece
 Embellished Swimsuits
 Glamorous Swimwear
 Tropical One-Piece
 Lace Bikini Sets
 Side-Tie Swimsuits
 Geometric Print Swimwear
 Ruffled Bikini Tops
 Sheer Mesh Swimsuits
 High-Neck Bikini
 Plunge One-Piece
 Cutout Halter Swimwear
 Bold Floral Bikini
 Metallic One-Piece
 Strapless Swimsuits
 Crochet Bikini Tops
 Textured One-Piece
 Fringed Swim Cover
 Sheer Panel Bikini
 Bold Color One-Piece
 Lace-Up One-Piece
 Tropical Halter Swimwear
 Ruffled Halter Bikini
 Cutout Strappy Swimsuits
 High-Leg One-Piece
 Mesh Trim Swimwear
 Bold Print One-Piece
 Tassel Halter Bikini
 Retro Halter Swimsuits
 Embroidered One-Piece
 Glitter Bikini Sets
 Tropical Cutout Swimwear
 Lace Trim One-Piece
 Strappy Halter Bikini
 Sheer Ruffle Swimsuits
 Bold Geometric Swimwear
 Cutout Plunge Bikini
 High-Waist One-Piece
 Mesh Panel Bikini
 Fringed One-Piece
 Sheer Cutout Swimwear
 Bold Striped Bikini
 Lace-Up Halter Swimsuits
 Tropical Strappy Swimwear
 Ruffled Plunge Bikini
 Cutout High-Neck Swimsuits
 Bold Floral One-Piece
 Metallic Halter Bikini
 Strapless One-Piece
 Crochet Halter Swimwear
 Textured Halter Bikini
 Fringed Halter Swimsuits
 Sheer Panel One-Piece
 Bold Color Halter Bikini
 Lace-Up Plunge Swimwear
 Tropical Cutout Bikini
 Ruffled Strappy Swimsuits
 Cutout Retro Swimwear
 High-Leg Halter Bikini
 Mesh Insert One-Piece
 Bold Print Halter Swimsuits
 Tassel Plunge Bikini
 Retro Cutout Swimwear
"""

Pullovers_l=r"""
 Women's Pullovers
 Knit Pullovers
 Wool Pullovers
 Cashmere Pullovers
 Cotton Pullovers
 Fleece Pullovers
 Lightweight Pullovers
 Heavyweight Pullovers
 Oversized Pullovers
 Slim Fit Pullovers
 Cropped Pullovers
 Longline Pullovers
 Turtleneck Pullovers
 V-Neck Pullovers
 Crew Neck Pullovers
 Scoop Neck Pullovers
 Mock Neck Pullovers
 Hooded Pullovers
 Zip-Up Pullovers
 Buttoned Pullovers
 Open-Front Pullovers
 Closed-Front Pullovers
 Belted Pullovers
 Wrap Pullovers
 Peplum Pullovers
 Tunic Pullovers
 Cropped Vest Pullovers
 Long Vest Pullovers
 Pullover Dresses
 Pullover Jackets
 Pullover Coats
 Pullover Cardigans
 Pullover Sweaters
 Pullover Tops
 Pullover Shirts
 Pullover Tunics
 Pullover Overcoats
 Pullover Ponchos
 Pullover Capes
 Pullover Kimonos
 Pullover Blouses
 Pullover Bodysuits
 Pullover Jumpsuits
 Pullover Rompers
 Pullover Skirts
 Pullover Pants
 Pullover Shorts
 Pullover Leggings
 Pullover Joggers
 Pullover Hoodies
 Pullover Sweatshirts
 Pullover T-Shirts
 Pullover Tank Tops
 Pullover Camisoles
 Pullover Bralettes
 Pullover Corsets
 Pullover Bustiers
 Pullover Gilets
 Pullover Vests
 Pullover Sleeves
 Pullover Armholes
 Pullover Hemlines
 Pullover Necklines
 Pullover Silhouettes
 Pullover Fabrics
 Pullover Patterns
 Pullover Designs
 Pullover Styles
 Pullover Trends
 Pullover Collections
 Pullover Outfits
 Pullover Ensembles
 Pullover Accessories
 Pullover Belts
 Pullover Buttons
 Pullover Zippers
 Pullover Snaps
 Pullover Hooks
 Pullover Loops
 Pullover Ties
 Pullover Straps
 Pullover Buckles
 Pullover Chains
 Pullover Charms
 Pullover Embellishments
 Pullover Appliques
 Pullover Patches
 Pullover Embroidery
 Pullover Beading
 Pullover Sequins
 Pullover Rhinestones
 Pullover Pearls
 Pullover Crystals
 Pullover Gems
 Pullover Stones
 Pullover Metals
 Pullover Leathers
 Pullover Suedes
 Pullover Furs
 Pullover Linings
 Pullover Interiors
 Pullover Exteriors
 Pullover Details
 Pullover Features
 Pullover Elements
 Pullover Components
 Pullover Parts
 Pullover Sections
 Pullover Layers
 Pullover Panels
 Pullover Inserts
 Pullover Overlays
 Pullover Underlays
 Pullover Trims
 Pullover Edges
 Pullover Borders
 Pullover Margins
 Pullover Perimeters
 Pullover Outlines
 Pullover Shapes
 Pullover Forms
 Pullover Structures
 Pullover Constructions
 Pullover Compositions
 Pullover Arrangements
 Pullover Configurations
 Pullover Organizations
 Pullover Systems
 Pullover Networks
 Pullover Frameworks
 Pullover Infrastructures
 Pullover Architectures
 Pullover Layouts
 Pullover Blueprints
 Pullover Schematics
 Pullover Diagrams
 Pullover Charts
 Pullover Graphs
 Pullover Maps
 Pullover Plans
 Pullover Strategies
 Pullover Tactics
 Pullover Methods
 Pullover Approaches
 Pullover Techniques
 Pullover Procedures
 Pullover Processes
 Pullover Operations
 Pullover Activities
 Pullover Actions
"""

Shorts_l=r"""
 Women's Shorts
 Denim Shorts
 High-Waisted Shorts
 Casual Shorts
 Formal Shorts
 Party Shorts
 Evening Shorts
 Work Shorts
 Outdoor Shorts
 Hiking Shorts
 Travel Shorts
 Fashion Shorts
 Trendy Shorts
 Vintage Shorts
 Modern Shorts
 Classic Shorts
 Contemporary Shorts
 Designer Shorts
 High-Street Shorts
 Budget Shorts
 Luxury Shorts
 Embroidered Shorts
 Patterned Shorts
 Solid Color Shorts
 Checked Shorts
 Striped Shorts
 Floral Shorts
 Animal Print Shorts
 Geometric Shorts
 Abstract Shorts
 Graphic Shorts
 Printed Shorts
 Embellished Shorts
 Beaded Shorts
 Sequined Shorts
 Rhinestone Shorts
 Pearl Shorts
 Crystal Shorts
 Gem Shorts
 Stone Shorts
 Metal Shorts
 Leather Trim Shorts
 Faux Fur Trim Shorts
 Shearling Trim Shorts
 Hooded Shorts
 Belted Shorts
 Zippered Shorts
 Buttoned Shorts
 Double-Breasted Shorts
 Single-Breasted Shorts
 Military Shorts
 Biker Shorts
 Motorcycle Shorts
 Aviator Shorts
 Cape Shorts
 Poncho Shorts
 Kimono Shorts
 Wrap Shorts
 Shacket Shorts
 Shearling Shorts
 Padded Shorts
 Lightweight Shorts
 Heavyweight Shorts
 Waterproof Shorts
 Insulated Shorts
 Reversible Shorts
 Metallic Shorts
 Shimmer Shorts
 Matte Shorts
 Textured Shorts
 Sheer Shorts
 Mesh Shorts
 Lace Shorts
 Crochet Shorts
 Knitted Shorts
 Woven Shorts
 Quilted Shorts
 Puffer Shorts
 Down Shorts
 Ski Shorts
 Snow Shorts
 Winter Shorts
 Spring Shorts
 Summer Shorts
 Fall Shorts
 Seasonal Shorts
 Denim Cutoff Shorts
 Lace Trim Shorts
 Paper Bag Waist Shorts
 Athletic Running Shorts
 Pleated Bermuda Shorts
 Stretch Cotton Shorts
 Side Slit Shorts
 Belted Chino Shorts
 Frayed Hem Shorts
 Tailored Linen Shorts
 Cargo Pocket Shorts
 High-Slit Denim Shorts
 Elastic Waist Shorts
 Embroidered Denim Shorts
 Cropped Casual Shorts
 Striped Lounge Shorts
 Button-Front Shorts
 Distressed Denim Shorts
 Wide Leg Shorts
 Tie-Dye Print Shorts
 Seamless Running Shorts
 Ruffled Hem Shorts
 Relaxed Fit Shorts
 Metallic Finish Shorts
 Drawstring Waist Shorts
 Floral Print Shorts
 Fitted Cycling Shorts
 Cropped Cargo Shorts
 Lace-Up Detail Shorts
 High-Rise Denim Shorts
 Pleated A-Line Shorts
 Mesh Panel Shorts
 Belted Paper Bag Shorts
 Embellished Hem Shorts
 Casual Lounge Shorts
 Stretch Denim Shorts
 Side Button Shorts
 Tropical Print Shorts
 High-Waist Bermuda Shorts
 Cropped Tailored Shorts
 Athletic Compression Shorts
 Ruffled Waist Shorts
 Relaxed Fit Denim Shorts
 Metallic Thread Shorts
 Drawstring Hem Shorts
 Floral Embroidered Shorts
 Fitted Running Shorts
 Cropped Wide Leg Shorts
 Lace-Up Waist Shorts
 High-Rise Cutoff Shorts
 Pleated Chino Shorts
 Mesh Lined Shorts
 Belted Casual Shorts
 Embellished Pocket Shorts
 Casual Cotton Shorts
 Stretch Linen Shorts
 Side Zip Shorts
 Tropical Floral Shorts
 High-Waist Paper Bag Shorts
 Cropped Pleated Shorts
 Athletic Mesh Shorts
 Ruffled Side Shorts
 Relaxed Fit Cargo Shorts
 Metallic Accent Shorts
 Drawstring Cargo Shorts
 Floral Lace Shorts
 Fitted Lounge Shorts
 Cropped Denim Shorts
 Lace-Up Side Shorts
 High-Rise Distressed Shorts
 Pleated Wide Leg Shorts
 Mesh Insert Shorts
 Belted High-Waist Shorts
 Embellished Waistband Shorts
 Casual Drawstring Shorts
 Stretch Paper Bag Shorts
 Side Tie Shorts
 Tropical Print Denim Shorts
 High-Waist Tailored Shorts
 Cropped Athletic Shorts
 Ruffled Hem Denim Shorts
 Relaxed Fit Bermuda Shorts
 Metallic Thread Denim Shorts
 Drawstring Lounge Shorts
 Floral Print Chino Shorts
 Fitted Cargo Shorts
 Cropped Lace Trim Shorts
 Lace-Up Front Shorts
 High-Rise Paper Bag Shorts
 Pleated Side Slit Shorts
 Mesh Panel Denim Shorts
 Belted Wide Leg Shorts
 Embellished Side Shorts
 Casual Pleated Shorts
 Stretch Bermuda Shorts
 Side Button Denim Shorts
 Tropical Floral Print Shorts
 High-Waist Cargo Shorts
 Cropped Ruffled Shorts
 Athletic Drawstring Shorts
 Ruffled Waistband Shorts
 Relaxed Fit Tailored Shorts
 Metallic Finish Denim Shorts
 Drawstring Paper Bag Shorts
 Floral Embroidered Denim Shorts
 Fitted High-Waist Shorts
 Cropped Mesh Shorts
 Lace-Up Back Shorts
 High-Rise Wide Leg Shorts
 Pleated Drawstring Shorts
 Mesh Lined Cargo Shorts
 Belted Side Slit Shorts
 Embellished Front Shorts
 Casual High-Waist Shorts
 Stretch Wide Leg Shorts
 Side Zip Denim Shorts
 Tropical Print Lounge Shorts
 High-Waist Pleated Shorts
 Cropped Athletic Mesh Shorts
 Ruffled Side Slit Shorts
 Relaxed Fit Paper Bag Shorts
 Metallic Thread Cargo Shorts
 Drawstring Tailored Shorts
 Floral Print Bermuda Shorts
 Fitted Side Tie Shorts
 Cropped Lace-Up Shorts
 Lace-Up Waistband Shorts
 High-Rise Ruffled Shorts
 Pleated Mesh Shorts
 Mesh Insert Cargo Shorts
 Belted Tropical Print Shorts
 Embellished Drawstring Shorts
 Casual Pleated Denim Shorts
 Stretch Side Slit Shorts
 Side Button Paper Bag Shorts
 Tropical Floral Cargo Shorts
 High-Waist Mesh Shorts
 Cropped Ruffled Denim Shorts
 Athletic Side Tie Shorts
 Ruffled Hem Paper Bag Shorts
 Relaxed Fit Wide Leg Shorts
 Metallic Finish Cargo Shorts
 Drawstring Pleated Shorts
 Floral Print Tailored Shorts
 Fitted Tropical Shorts
 Cropped Lace-Up Denim Shorts
 Lace-Up Side Slit Shorts
 High-Rise Embroidered Shorts
 Pleated Tropical Print Shorts
"""

Swimsuit_l=r"""
 Women's Swimsuits
 Bikini Sets
 One-Piece Swimwear
 High-Waisted Bikini
 Halter Neck Swimsuit
 Push-Up Bikini
 Tankini Outfits
 Sheer Cover-Ups
 Crochet Bikini
 Ruffled Swimsuits
 Mesh Swimwear
 Cut-Out Designs
 Strapless Bikini
 Printed Swimsuits
 Vintage Swimwear
 Sporty Bikini
 Lace-Up Swimsuits
 Tropical Prints
 High-Cut Bottoms
 Plunge Neckline
 Bandeau Bikini
 Tied Swimsuits
 Bold Color Swimwear
 Geometric Patterns
 Longline Tops
 Cheeky Bottoms
 Off-Shoulder Swimwear
 Metallic Swimsuits
 Animal Print Bikini
 Cropped Swim Top
 Side-Tie Bottoms
 Boho Swimsuits
 Glitter Swimwear
 Underwire Bikini
 Retro Swimsuits
 Solid Color Swimwear
 Embroidered Bikini
 Ruffle Bikini Tops
 Mesh Panel Swimsuits
 High-Neck Swimwear
 Low-Back Swimsuits
 Two-Tone Bikini
 Adjustable Swimwear
 Tassel Bikini Sets
 Pastel Swimsuits
 Neon Swimwear
 Shimmer Bikini
 Lace Trim Swimsuits
 Belted One-Piece
 Triangle Bikini
 Wrap Swimwear
 Crochet Cover-Ups
 Strappy Swimsuits
 Textured Swimwear
 Seamless Bikini
 Reversible Swimsuits
 Halter Bikini Tops
 Side-Cut Swimwear
 Fringed Bikini
 Sheer Panel Swimsuits
 Bold Print Swimwear
 Crisscross Bikini
 Cutout One-Piece
 Tied Halter Swimsuits
 Metallic Sheen Swimwear
 High-Leg Swimsuits
 Ruffled One-Piece
 Tropical Bikini
 Lace-Up Bikini
 Sporty One-Piece
 Floral Print Swimwear
 Deep V-Neck Swimsuits
 Color Block Bikini
 Cropped Swim Cover
 Strappy One-Piece
 Sheer Swim Cover
 Bold Striped Swimwear
 Cutout Bikini Tops
 High-Waist Swimsuits
 Mesh Insert Swimwear
 Tassel Trim Bikini
 Retro One-Piece
 Embellished Swimsuits
 Glamorous Swimwear
 Tropical One-Piece
 Lace Bikini Sets
 Side-Tie Swimsuits
 Geometric Print Swimwear
 Ruffled Bikini Tops
 Sheer Mesh Swimsuits
 High-Neck Bikini
 Plunge One-Piece
 Cutout Halter Swimwear
 Bold Floral Bikini
 Metallic One-Piece
 Strapless Swimsuits
 Crochet Bikini Tops
 Textured One-Piece
 Fringed Swim Cover
 Sheer Panel Bikini
 Bold Color One-Piece
 Lace-Up One-Piece
 Tropical Halter Swimwear
 Ruffled Halter Bikini
 Cutout Strappy Swimsuits
 High-Leg One-Piece
 Mesh Trim Swimwear
 Bold Print One-Piece
 Tassel Halter Bikini
 Retro Halter Swimsuits
 Embroidered One-Piece
 Glitter Bikini Sets
 Tropical Cutout Swimwear
 Lace Trim One-Piece
 Strappy Halter Bikini
 Sheer Ruffle Swimsuits
 Bold Geometric Swimwear
 Cutout Plunge Bikini
 High-Waist One-Piece
 Mesh Panel Bikini
 Fringed One-Piece
 Sheer Cutout Swimwear
 Bold Striped Bikini
 Lace-Up Halter Swimsuits
 Tropical Strappy Swimwear
 Ruffled Plunge Bikini
 Cutout High-Neck Swimsuits
 Bold Floral One-Piece
 Metallic Halter Bikini
 Strapless One-Piece
 Crochet Halter Swimwear
 Textured Halter Bikini
 Fringed Halter Swimsuits
 Sheer Panel One-Piece
 Bold Color Halter Bikini
 Lace-Up Plunge Swimwear
 Tropical Cutout Bikini
 Ruffled Strappy Swimsuits
 Cutout Retro Swimwear
 High-Leg Halter Bikini
 Mesh Insert One-Piece
 Bold Print Halter Swimsuits
 Tassel Plunge Bikini
 Retro Cutout Swimwear
 High-Waist Halter Bikini
 Sheer Mesh One-Piece
 Bold Floral Halter Swimsuits
 Metallic Cutout Bikini
 Strapless Halter Swimwear
 Crochet Plunge Bikini
"""

TShirts_l=r"""
 Women's T-Shirts
 Casual T-Shirts
 Graphic T-Shirts
 Plain T-Shirts
 Striped T-Shirts
 Printed T-Shirts
 Embroidered T-Shirts
 Vintage T-Shirts
 Oversized T-Shirts
 Slim Fit T-Shirts
 Cropped T-Shirts
 Longline T-Shirts
 V-Neck T-Shirts
 Crew Neck T-Shirts
 Scoop Neck T-Shirts
 Mock Neck T-Shirts
 Raglan T-Shirts
 Baseball T-Shirts
 Pocket T-Shirts
 Tie-Dye T-Shirts
 Abstract T-Shirts
 Floral T-Shirts
 Animal Print T-Shirts
 Geometric T-Shirts
 Polka Dot T-Shirts
 Letter Print T-Shirts
 Logo T-Shirts
 Band T-Shirts
 Retro T-Shirts
 Bohemian T-Shirts
 Minimalist T-Shirts
 Artistic T-Shirts
 Inspirational T-Shirts
 Funny T-Shirts
 Slogan T-Shirts
 Quote T-Shirts
 Cartoon T-Shirts
 Pop Culture T-Shirts
 Music T-Shirts
 Movie T-Shirts
 Sports T-Shirts
 Fitness T-Shirts
 Yoga T-Shirts
 Gym T-Shirts
 Running T-Shirts
 Cycling T-Shirts
 Travel T-Shirts
 Festival T-Shirts
 Holiday T-Shirts
 Seasonal T-Shirts
 Summer T-Shirts
 Winter T-Shirts
 Spring T-Shirts
 Fall T-Shirts
 Lightweight T-Shirts
 Heavyweight T-Shirts
 Organic T-Shirts
 Cotton T-Shirts
 Linen T-Shirts
 Polyester T-Shirts
 Blended T-Shirts
 Stretch T-Shirts
 Breathable T-Shirts
 Moisture-Wicking T-Shirts
 Quick-Dry T-Shirts
 UV Protection T-Shirts
 Eco-Friendly T-Shirts
 Sustainable T-Shirts
 Recycled T-Shirts
 Fair Trade T-Shirts
 Relaxed Fit T-Shirts
 Fitted T-Shirts
 Boxed Fit T-Shirts
 Drop Shoulder T-Shirts
 Cropped Fit T-Shirts
 High-Low T-Shirts
 Asymmetrical T-Shirts
 Layered T-Shirts
 Ruffled T-Shirts
 Lace Trim T-Shirts
 Sheer T-Shirts
 Mesh T-Shirts
 Cut-Out T-Shirts
 Side Slit T-Shirts
 Backless T-Shirts
 Cold Shoulder T-Shirts
 Off-Shoulder T-Shirts
 Halter Neck T-Shirts
 Wrap T-Shirts
 Peplum T-Shirts
 Tunic T-Shirts
 Cropped Vest T-Shirts
 Long Vest T-Shirts
 T-Shirt Dresses
 T-Shirt Jackets
 T-Shirt Coats
 T-Shirt Cardigans
 T-Shirt Sweaters
 T-Shirt Tops
 T-Shirt Shirts
 T-Shirt Tunics
 T-Shirt Overcoats
 T-Shirt Ponchos
 T-Shirt Capes
 T-Shirt Kimonos
 T-Shirt Blouses
 T-Shirt Bodysuits
 T-Shirt Jumpsuits
 T-Shirt Rompers
 T-Shirt Skirts
 T-Shirt Pants
 T-Shirt Shorts
 T-Shirt Leggings
 T-Shirt Joggers
 T-Shirt Hoodies
 T-Shirt Sweatshirts
 T-Shirt Tank Tops
 T-Shirt Camisoles
 T-Shirt Bralettes
 T-Shirt Corsets
 T-Shirt Bustiers
 T-Shirt Gilets
 T-Shirt Vests
 T-Shirt Sleeves
 T-Shirt Armholes
 T-Shirt Hemlines
 T-Shirt Necklines
 T-Shirt Silhouettes
 T-Shirt Fabrics
 T-Shirt Patterns
 T-Shirt Designs
 T-Shirt Styles
 T-Shirt Trends
 T-Shirt Collections
 T-Shirt Outfits
 T-Shirt Ensembles
 T-Shirt Accessories
 T-Shirt Belts
 T-Shirt Buttons
 T-Shirt Zippers
 T-Shirt Snaps
 T-Shirt Hooks
 T-Shirt Loops
 T-Shirt Ties
 T-Shirt Straps
 T-Shirt Buckles
 T-Shirt Chains
 T-Shirt Charms
 T-Shirt Embellishments
 T-Shirt Appliques
"""

Tank_Tops_Camis_l=r"""
 Women's Tank Tops
 Casual Tank Tops
 Formal Tank Tops
 Party Tank Tops
 Evening Tank Tops
 Work Tank Tops
 Outdoor Tank Tops
 Hiking Tank Tops
 Travel Tank Tops
 Fashion Tank Tops
 Trendy Tank Tops
 Vintage Tank Tops
 Modern Tank Tops
 Classic Tank Tops
 Contemporary Tank Tops
 Designer Tank Tops
 High-Street Tank Tops
 Budget Tank Tops
 Luxury Tank Tops
 Embroidered Tank Tops
 Patterned Tank Tops
 Solid Color Tank Tops
 Checked Tank Tops
 Striped Tank Tops
 Floral Tank Tops
 Animal Print Tank Tops
 Geometric Tank Tops
 Abstract Tank Tops
 Graphic Tank Tops
 Printed Tank Tops
 Embellished Tank Tops
 Beaded Tank Tops
 Sequined Tank Tops
 Rhinestone Tank Tops
 Pearl Tank Tops
 Crystal Tank Tops
 Gem Tank Tops
 Stone Tank Tops
 Metal Tank Tops
 Leather Trim Tank Tops
 Faux Fur Trim Tank Tops
 Shearling Trim Tank Tops
 Hooded Tank Tops
 Belted Tank Tops
 Zippered Tank Tops
 Buttoned Tank Tops
 Double-Breasted Tank Tops
 Single-Breasted Tank Tops
 Military Tank Tops
 Biker Tank Tops
 Motorcycle Tank Tops
 Aviator Tank Tops
 Cape Tank Tops
 Poncho Tank Tops
 Kimono Tank Tops
 Wrap Tank Tops
 Shacket Tank Tops
 Shearling Tank Tops
 Padded Tank Tops
 Lightweight Tank Tops
 Heavyweight Tank Tops
 Waterproof Tank Tops
 Insulated Tank Tops
 Reversible Tank Tops
 Metallic Tank Tops
 Shimmer Tank Tops
 Matte Tank Tops
 Textured Tank Tops
 Sheer Tank Tops
 Mesh Tank Tops
 Lace Tank Tops
 Crochet Tank Tops
 Knitted Tank Tops
 Woven Tank Tops
 Quilted Tank Tops
 Puffer Tank Tops
 Down Tank Tops
 Ski Tank Tops
 Snow Tank Tops
 Winter Tank Tops
 Spring Tank Tops
 Summer Tank Tops
 Fall Tank Tops
 Seasonal Tank Tops
 Sleeveless Tank Top
 Lace Trim Camisole
 Ribbed Tank Top
 Strappy Cami Top
 Slim Fit Tank
 Layered Camisole
 High Neck Tank
 Satin Slip Camisole
 Cropped Tank Top
 Embroidered Cami
 Built-In Bra Tank
 Sheer Panel Camisole
 Racerback Tank Top
 Lace Bodice Camisole
 Muscle Tank Top
 Silk Blend Camisole
 Wide Strap Tank
 Ruffled Hem Cami
 Seamless Tank Top
 Strapless Camisole
 Scoop Neck Tank
 Embellished Cami Top
 Longline Tank Top
 Lace Back Camisole
 Cotton Blend Tank
 Satin Tie Camisole
 Fitted Tank Dress
 Mesh Insert Cami
 Halter Neck Tank
 Bow Detail Camisole
 Relaxed Fit Tank
 Layered Ruffle Cami
 Spaghetti Strap Tank
 Embroidered Camisole
 Cropped Muscle Tank
 Sheer Yoke Camisole
 Ribbed Cami Top
 Cutout Detail Tank
 Lace Trim Slip Cami
 High-Low Hem Tank
 Satin Camisole Top
 Side Slit Tank Top
 Strappy Lace Cami
 Fitted Sleeveless Tank
 Metallic Thread Camisole
 Oversized Tank Top
 Ruffled Straps Cami
 Longline Camisole
 Cropped Racerback Tank
 Embellished Neckline Cami
 Seamless Camisole Top
 Mesh Panel Tank
 Lace Trim Tank Top
 Silk Slip Camisole
 Fitted Ribbed Tank
 Sheer Overlay Cami
 Halter Camisole Top
 Cropped Sleeveless Tank
 Embroidered Straps Cami
 Relaxed Fit Camisole
 Layered Tank Dress
 Lace Bodice Tank
 Satin Slip Tank Top
 Wide Neckline Cami
 Muscle Fit Tank
 Ruffled Neckline Camisole
 Spaghetti Strap Cami
 Cutout Back Tank
 Embellished Camisole
 Longline Sleeveless Tank
 Sheer Panel Tank Top
 Lace Trim Halter Cami
 Ribbed Muscle Tank
 Satin Camisole Dress
 Cropped Spaghetti Tank
 Embroidered Slip Cami
 Fitted Layered Tank
 Mesh Insert Tank Top
 Strappy Silk Camisole
 High Neck Camisole
 Relaxed Fit Sleeveless Tank
 Lace Back Tank Top
 Ruffled Hem Tank
 Seamless Camisole Dress
 Cropped Halter Tank
 Sheer Yoke Tank Top
 Embellished Straps Cami
 Longline Ribbed Tank
 Satin Blend Camisole
 Cutout Side Tank
 Lace Trim Muscle Tank
 Silk Slip Tank Top
 Fitted Strappy Cami
 Mesh Panel Camisole
 Layered Sleeveless Tank
 Embroidered Halter Cami
 Relaxed Fit Tank Dress
 Ruffled Neckline Tank
 Spaghetti Strap Slip Cami
 High-Low Hem Camisole
 Cropped Racerback Cami
 Sheer Overlay Tank
 Lace Bodice Camisole Dress
 Ribbed Sleeveless Tank
 Satin Tie Front Cami
 Fitted Muscle Tank
 Embellished Slip Camisole
 Longline Halter Tank
 Mesh Insert Camisole
 Strappy Lace Tank
 Layered Ruffled Cami
 Cutout Detail Camisole
 Lace Trim Sleeveless Tank
 Silk Blend Tank Top
 Cropped Spaghetti Cami
 Embroidered Muscle Tank
 Relaxed Fit Halter Top
 Sheer Panel Camisole Dress
 Ruffled Straps Tank
 Seamless Sleeveless Top
 High Neck Camisole Dress
 Lace Back Muscle Tank
 Satin Slip Sleeveless Top
 Fitted Ribbed Camisole
 Mesh Yoke Tank
 Embellished Halter Cami
 Longline Spaghetti Tank
 Cutout Back Camisole
 Lace Trim Slip Tank
 Silk Camisole Top
 Cropped Layered Tank
 Sheer Overlay Camisole
 Strappy Ribbed Cami
 Ruffled Hem Camisole
 Seamless Halter Tank
 High-Low Hem Tank Dress
 Embroidered Sleeveless Top
 Relaxed Fit Muscle Tank
 Lace Bodice Tank Top
 Satin Blend Sleeveless Top
 Fitted Strappy Tank
 Mesh Panel Halter Cami
 Layered Ruffled Tank
 Cutout Side Camisole
 Lace Trim Muscle Cami
 Silk Slip Sleeveless Top
 Cropped Embellished Tank
 Sheer Yoke Camisole Dress
 Ribbed Halter Tank
 Strappy Lace Camisole
"""

Tops_l=r"""
 Women's Tops
 Casual Tops
 Formal Tops
 Party Tops
 Evening Tops
 Work Tops
 Outdoor Tops
 Hiking Tops
 Travel Tops
 Fashion Tops
 Trendy Tops
 Vintage Tops
 Modern Tops
 Classic Tops
 Contemporary Tops
 Designer Tops
 High-Street Tops
 Budget Tops
 Luxury Tops
 Embroidered Tops
 Patterned Tops
 Solid Color Tops
 Checked Tops
 Striped Tops
 Floral Tops
 Animal Print Tops
 Geometric Tops
 Abstract Tops
 Graphic Tops
 Printed Tops
 Embellished Tops
 Beaded Tops
 Sequined Tops
 Rhinestone Tops
 Pearl Tops
 Crystal Tops
 Gem Tops
 Stone Tops
 Metal Tops
 Leather Trim Tops
 Faux Fur Trim Tops
 Shearling Trim Tops
 Hooded Tops
 Belted Tops
 Zippered Tops
 Buttoned Tops
 Double-Breasted Tops
 Single-Breasted Tops
 Military Tops
 Biker Tops
 Motorcycle Tops
 Aviator Tops
 Cape Tops
 Poncho Tops
 Kimono Tops
 Wrap Tops
 Shacket Tops
 Shearling Tops
 Padded Tops
 Lightweight Tops
 Heavyweight Tops
 Waterproof Tops
 Insulated Tops
 Reversible Tops
 Metallic Tops
 Shimmer Tops
 Matte Tops
 Textured Tops
 Sheer Tops
 Mesh Tops
 Lace Tops
 Crochet Tops
 Knitted Tops
 Woven Tops
 Quilted Tops
 Puffer Tops
 Down Tops
 Ski Tops
 Snow Tops
 Winter Tops
 Spring Tops
 Summer Tops
 Fall Tops
 Seasonal Tops
 Floral Print Blouse
 Striped Crop Top
 Lace Trim Tee
 Off-Shoulder Top
 Ruffled Sleeve Shirt
 High Neck Blouse
 Wrap Front Top
 Embroidered Peplum
 Mesh Panel Tee
 Button-Down Shirt
 Cold Shoulder Top
 Tie-Waist Blouse
 Crochet Detail Top
 Halter Neck Tank
 Asymmetric Hem Top
 Velvet Bodysuit
 Sheer Overlay Blouse
 Belted Tunic Top
 Pleated Front Shirt
 Graphic Print Tee
 Longline Tank Top
 Chiffon Bell Sleeve
 Knit Crop Sweater
 Faux Leather Top
 Smocked Bodice Blouse
 Puff Sleeve Shirt
 Sequin Embellished Top
 Ribbed Knit Tee
 Layered Ruffle Blouse
 Satin Camisole Top
 Cutout Detail Shirt
 Oversized Button-Up
 Cropped Hoodie Top
 Tie-Dye Tee
 Metallic Thread Top
 Bow Front Blouse
 Thermal Henley Top
 Flounce Hem Shirt
 Mesh Insert Tank
 Turtleneck Sweater
 Shirred Waist Top
 Embellished Collar Blouse
 Relaxed Fit Tee
 Keyhole Back Top
 Linen Blend Shirt
 Cropped Pullover Sweater
 Glitter Accent Top
 Tiered Ruffle Blouse
 Scoop Neck Tank
 Quilted Detail Top
 Side Slit Tee
 Printed Kimono Top
 Structured Peplum Shirt
 Ribbed Crop Top
 Sheer Yoke Blouse
 Fitted Camisole
 Oversized Graphic Tee
 Twist Front Top
 Long Sleeve Bodysuit
 Embroidered Tank Top
 Layered Tunic Shirt
 Crochet Back Top
 Metallic Finish Blouse
 Relaxed Henley Tee
 Asymmetric Neckline Top
 Faux Fur Trim Shirt
 Belted Wrap Blouse
 Mesh Longline Top
 Button-Front Sweater
 Floral Appliqué Tee
 High-Low Hem Top
 Lace-Up Detail Shirt
 Cropped Hooded Top
 Pleated Sleeve Blouse
 Ribbed Bodysuit
 Oversized Pocket Tee
 Cutout Shoulder Top
 Chiffon Wrap Blouse
 Embroidered Crop Top
 Longline Cardigan Top
 Fitted Tank Dress
 Ruffled Hem Shirt
 Metallic Lace Top
 Tie-Neck Blouse
 Cropped Sweatshirt Top
 Sheer Panel Tee
 Asymmetric Hem Blouse
 Knit Mock Neck Top
 Belted Tunic Shirt
 Floral Lace Top
 Oversized Flannel Shirt
 Cropped Puff Sleeve
 Embellished Tank
 Longline Blazer Top
 Ribbed Knit Sweater
 Side Tie Tee
 Velvet Trim Blouse
 Fitted Polo Top
 Layered Chiffon Shirt
 Cropped Denim Top
 Mesh Sleeve Tee
 Ruffled Collar Blouse
 High-Low Sweater
 Embroidered Peasant Top
 Belted Wrap Shirt
 Lace Insert Tank
 Oversized V-Neck Tee
 Cutout Back Top
 Floral Chiffon Blouse
 Ribbed Crop Sweater
 Metallic Thread Tank
 Button-Front Blouse
 Cropped Hoodie Dress
 Sheer Yoke Tee
 Asymmetric Ruffle Top
 Faux Leather Shirt
 Tie-Waist Tunic
 Embellished Sleeve Blouse
 Longline Tank Dress
 Crochet Trim Top
 Oversized Graphic Sweater
 Ruffled Peplum Shirt
 Metallic Lace Blouse
 Side Slit Tank
 Belted Chiffon Top
 Embroidered Henley Tee
 Layered Ruffle Shirt
 Cropped Faux Fur Top
 Sheer Panel Blouse
 Ribbed Mock Neck
 Floral Print Tank
 Oversized Button-Down
 Cutout Sleeve Top
 Lace-Up Blouse
 Cropped Sweater Vest
 Metallic Finish Tee
 Asymmetric Hem Shirt
 Fitted Wrap Top
 Embellished Collar Tee
 Longline Cardigan Shirt
 Ruffled Sleeve Blouse
 Cropped Hooded Sweater
 Sheer Yoke Tank
 Belted Peplum Top
 Embroidered Floral Blouse
 Oversized Pocket Shirt
 Cutout Detail Tank
 Lace Trim Sweater
 High-Low Hem Blouse
 Ribbed Bodysuit Top
"""

Trench_l=r"""
 Women's Trench Coats
 Classic Trench Coat
 Double-Breasted Trench
 Single-Breasted Trench
 Belted Trench Coat
 Waterproof Trench Coat
 Wool Trench Coat
 Cotton Trench Coat
 Polyester Trench Coat
 Lightweight Trench Coat
 Heavyweight Trench Coat
 Longline Trench Coat
 Cropped Trench Coat
 Oversized Trench Coat
 Slim Fit Trench Coat
 Relaxed Fit Trench Coat
 Tailored Trench Coat
 Casual Trench Coat
 Formal Trench Coat
 Vintage Trench Coat
 Modern Trench Coat
 Trendy Trench Coat
 Designer Trench Coat
 Luxury Trench Coat
 Budget Trench Coat
 High-Street Trench Coat
 Embroidered Trench Coat
 Patterned Trench Coat
 Solid Color Trench Coat
 Checked Trench Coat
 Striped Trench Coat
 Floral Trench Coat
 Animal Print Trench Coat
 Geometric Trench Coat
 Abstract Trench Coat
 Graphic Trench Coat
 Printed Trench Coat
 Embellished Trench Coat
 Beaded Trench Coat
 Sequined Trench Coat
 Rhinestone Trench Coat
 Pearl Trench Coat
 Crystal Trench Coat
 Gem Trench Coat
 Stone Trench Coat
 Metal Trench Coat
 Leather Trim Trench Coat
 Faux Fur Trim Trench Coat
 Shearling Trim Trench Coat
 Hooded Trench Coat
 Zippered Trench Coat
 Buttoned Trench Coat
 Open-Front Trench Coat
 Closed-Front Trench Coat
 Wrap Trench Coat
 Peplum Trench Coat
 Tunic Trench Coat
 Cropped Vest Trench Coat
 Long Vest Trench Coat
 Trench Coat Dress
 Trench Coat Jacket
 Trench Coat Blazer
 Trench Coat Cardigan
 Trench Coat Sweater
 Trench Coat Top
 Trench Coat Shirt
 Trench Coat Tunic
 Trench Coat Overcoat
 Trench Coat Poncho
 Trench Coat Cape
 Trench Coat Kimono
 Trench Coat Blouse
 Trench Coat Bodysuit
 Trench Coat Jumpsuit
 Trench Coat Romper
 Trench Coat Skirt
 Trench Coat Pants
 Trench Coat Shorts
 Trench Coat Leggings
 Trench Coat Joggers
 Trench Coat Hoodie
 Trench Coat Sweatshirt
 Trench Coat T-Shirt
 Trench Coat Tank Top
 Trench Coat Camisole
 Trench Coat Bralette
 Trench Coat Corset
 Trench Coat Bustier
 Trench Coat Gilet
 Trench Coat Vest
 Trench Coat Sleeves
 Trench Coat Armholes
 Trench Coat Hemlines
 Trench Coat Necklines
 Trench Coat Silhouettes
 Trench Coat Fabrics
 Trench Coat Patterns
 Trench Coat Designs
 Trench Coat Styles
 Trench Coat Trends
 Trench Coat Collections
 Trench Coat Outfits
 Trench Coat Ensembles
 Trench Coat Accessories
 Trench Coat Belts
 Trench Coat Buttons
 Trench Coat Zippers
 Trench Coat Snaps
 Trench Coat Hooks
 Trench Coat Loops
 Trench Coat Ties
 Trench Coat Straps
 Trench Coat Buckles
 Trench Coat Chains
 Trench Coat Charms
 Trench Coat Embellishments
 Trench Coat Appliques
 Trench Coat Patches
 Trench Coat Embroidery
 Trench Coat Beading
 Trench Coat Sequins
 Trench Coat Rhinestones
 Trench Coat Pearls
 Trench Coat Crystals
 Trench Coat Gems
 Trench Coat Stones
 Trench Coat Metals
 Trench Coat Leathers
 Trench Coat Suedes
 Trench Coat Furs
 Trench Coat Linings
 Trench Coat Interiors
 Trench Coat Exteriors
 Trench Coat Details
 Trench Coat Features
 Trench Coat Elements
 Trench Coat Components
 Trench Coat Parts
 Trench Coat Sections
 Trench Coat Layers
 Trench Coat Panels
 Trench Coat Inserts
 Trench Coat Overlays
 Trench Coat Underlays
 Trench Coat Trims
 Trench Coat Edges
 Trench Coat Borders
 Trench Coat Margins
 Trench Coat Perimeters
 Trench Coat Outlines
"""

Waistcoats_l=r"""
 Women's Waistcoats
 Slim Fit Waistcoat
 Tailored Waistcoats
 Casual Waistcoats
 Formal Waistcoats
 Double-Breasted Waistcoat
 Single-Breasted Waistcoat
 Velvet Waistcoats
 Linen Waistcoats
 Wool Waistcoats
 Silk Waistcoats
 Embroidered Waistcoats
 Patterned Waistcoats
 Solid Color Waistcoats
 Checked Waistcoats
 Striped Waistcoats
 Floral Waistcoats
 Vintage Waistcoats
 Modern Waistcoats
 Cropped Waistcoats
 Longline Waistcoats
 Belted Waistcoats
 Buttoned Waistcoats
 Zippered Waistcoats
 High-Neck Waistcoats
 V-Neck Waistcoats
 Lapel Waistcoats
 Collared Waistcoats
 Sleeveless Waistcoats
 Lightweight Waistcoats
 Heavyweight Waistcoats
 Quilted Waistcoats
 Padded Waistcoats
 Fitted Waistcoats
 Oversized Waistcoats
 Stretch Waistcoats
 Elastic Waistcoats
 Adjustable Waistcoats
 Reversible Waistcoats
 Metallic Waistcoats
 Shimmer Waistcoats
 Matte Waistcoats
 Textured Waistcoats
 Sheer Waistcoats
 Mesh Waistcoats
 Lace Waistcoats
 Crochet Waistcoats
 Knitted Waistcoats
 Woven Waistcoats
 Denim Waistcoats
 Leather Waistcoats
 Faux Fur Waistcoats
 Hooded Waistcoats
 Pocketed Waistcoats
 Buttonless Waistcoats
 Asymmetrical Waistcoats
 Layered Waistcoats
 Tiered Waistcoats
 Ruffled Waistcoats
 Pleated Waistcoats
 Draped Waistcoats
 Belted Back Waistcoats
 Side-Tie Waistcoats
 Front-Tie Waistcoats
 Backless Waistcoats
 Cut-Out Waistcoats
 High-Slit Waistcoats
 Low-Back Waistcoats
 Open-Front Waistcoats
 Closed-Front Waistcoats
 Wrap Waistcoats
 Peplum Waistcoats
 Tunic Waistcoats
 Cropped Vest Waistcoats
 Long Vest Waistcoats
 Waistcoat Dresses
 Waistcoat Jackets
 Waistcoat Coats
 Waistcoat Blazers
 Waistcoat Cardigans
 Waistcoat Sweaters
 Waistcoat Tops
 Waistcoat Shirts
 Waistcoat Tunics
 Waistcoat Overcoats
 Waistcoat Ponchos
 Waistcoat Capes
 Waistcoat Kimonos
 Waistcoat Blouses
 Waistcoat Bodysuits
 Waistcoat Jumpsuits
 Waistcoat Rompers
 Waistcoat Skirts
 Waistcoat Pants
 Waistcoat Shorts
 Waistcoat Leggings
 Waistcoat Joggers
 Waistcoat Hoodies
 Waistcoat Sweatshirts
 Waistcoat T-Shirts
 Waistcoat Tank Tops
 Waistcoat Camisoles
 Waistcoat Bralettes
 Waistcoat Corsets
 Waistcoat Bustiers
 Waistcoat Gilets
 Waistcoat Vests
 Waistcoat Sleeves
 Waistcoat Armholes
 Waistcoat Hemlines
 Waistcoat Necklines
 Waistcoat Silhouettes
 Waistcoat Fabrics
 Waistcoat Patterns
 Waistcoat Designs
 Waistcoat Styles
 Waistcoat Trends
 Waistcoat Collections
 Waistcoat Outfits
 Waistcoat Ensembles
 Waistcoat Accessories
 Waistcoat Belts
 Waistcoat Buttons
 Waistcoat Zippers
 Waistcoat Snaps
 Waistcoat Hooks
 Waistcoat Loops
 Waistcoat Ties
 Waistcoat Straps
 Waistcoat Buckles
 Waistcoat Chains
 Waistcoat Charms
 Waistcoat Embellishments
 Waistcoat Appliques
 Waistcoat Patches
 Waistcoat Embroidery
 Waistcoat Beading
 Waistcoat Sequins
 Waistcoat Rhinestones
 Waistcoat Pearls
 Waistcoat Crystals
 Waistcoat Gems
 Waistcoat Stones
 Waistcoat Metals
 Waistcoat Leathers
 Waistcoat Suedes
 Waistcoat Furs
 Waistcoat Linings
 Waistcoat Interiors
 Waistcoat Exteriors
"""

# 2601
Winter_Coats_l=r"""
 Women's Winter Coats
 Heavyweight Winter Coats
 Insulated Winter Coats
 Down Winter Coats
 Puffer Winter Coats
 Quilted Winter Coats
 Wool Winter Coats
 Faux Fur Winter Coats
 Parka Winter Coats
 Trench Winter Coats
 Pea Winter Coats
 Duffle Winter Coats
 Hooded Winter Coats
 Belted Winter Coats
 Zippered Winter Coats
 Buttoned Winter Coats
 Double-Breasted Winter Coats
 Single-Breasted Winter Coats
 Military Winter Coats
 Biker Winter Coats
 Motorcycle Winter Coats
 Aviator Winter Coats
 Cape Winter Coats
 Poncho Winter Coats
 Kimono Winter Coats
 Wrap Winter Coats
 Shacket Winter Coats
 Shearling Winter Coats
 Padded Winter Coats
 Lightweight Winter Coats
 Waterproof Winter Coats
 Reversible Winter Coats
 Metallic Winter Coats
 Shimmer Winter Coats
 Matte Winter Coats
 Textured Winter Coats
 Sheer Winter Coats
 Mesh Winter Coats
 Lace Winter Coats
 Crochet Winter Coats
 Knitted Winter Coats
 Woven Winter Coats
 Quilted Jackets Winter
 Puffer Jackets Winter
 Down Jackets Winter
 Ski Jackets Winter
 Snow Jackets Winter
 Winter Jackets
 Spring Jackets Winter
 Summer Jackets Winter
 Fall Jackets Winter
 Seasonal Jackets Winter
 Casual Jackets Winter
 Formal Jackets Winter
 Party Jackets Winter
 Evening Jackets Winter
 Work Jackets Winter
 Outdoor Jackets Winter
 Hiking Jackets Winter
 Travel Jackets Winter
 Fashion Jackets Winter
 Trendy Jackets Winter
 Vintage Jackets Winter
 Modern Jackets Winter
 Classic Jackets Winter
 Contemporary Jackets Winter
 Designer Jackets Winter
 High-Street Jackets Winter
 Budget Jackets Winter
 Luxury Jackets Winter
 Embroidered Jackets Winter
 Patterned Jackets Winter
 Solid Color Jackets Winter
 Checked Jackets Winter
 Striped Jackets Winter
 Floral Jackets Winter
 Animal Print Jackets Winter
 Geometric Jackets Winter
 Abstract Jackets Winter
 Graphic Jackets Winter
 Printed Jackets Winter
 Embellished Jackets Winter
 Beaded Jackets Winter
 Sequined Jackets Winter
 Rhinestone Jackets Winter
 Pearl Jackets Winter
 Crystal Jackets Winter
 Gem Jackets Winter
 Stone Jackets Winter
 Metal Jackets Winter
 Leather Trim Jackets Winter
 Faux Fur Trim Jackets Winter
 Shearling Trim Jackets Winter
 Hooded Coats Winter
 Belted Coats Winter
 Zippered Coats Winter
 Buttoned Coats Winter
 Double-Breasted Coats Winter
 Single-Breasted Coats Winter
 Military Coats Winter
 Biker Coats Winter
 Motorcycle Coats Winter
 Aviator Coats Winter
 Pea Coats Winter
 Duffle Coats Winter
 Cape Coats Winter
 Poncho Coats Winter
 Kimono Coats Winter
 Wrap Coats Winter
 Shacket Coats Winter
 Shearling Coats Winter
 Padded Coats Winter
 Lightweight Coats Winter
 Heavyweight Coats Winter
 Waterproof Coats Winter
 Insulated Coats Winter
 Reversible Coats Winter
 Metallic Coats Winter
 Shimmer Coats Winter
 Matte Coats Winter
 Textured Coats Winter
 Sheer Coats Winter
 Mesh Coats Winter
 Lace Coats Winter
 Crochet Coats Winter
 Knitted Coats Winter
 Woven Coats Winter
 Classic Jackets
"""

Blazers_l=r"""
 Stylish Women’s Blazers
 Elegant Blazers for Women
 Casual Blazer Look
 Formal Women’s Blazers
 Classic Blazer Style
 Office Blazer Outfits
 Trendy Women’s Blazers
 Chic Blazers for Women
 Women’s Blazer Collection
 Slim Fit Blazer
 Tailored Blazer for Women
 Vintage Blazers for Women
 Fitted Blazer Look
 Women’s Long Blazer
 Black Blazer Jacket
 Buttoned Women’s Blazer
 Stylish Blazer Jacket
 Casual Blazer Style
 Printed Blazers for Women
 Checkered Blazer Jacket
 Women’s Double-breasted Blazer
 Oversized Women’s Blazer
 Blazers for Business Wear
 Blazer Dress for Women
 Classic Blazer Jacket
 Button Detail Blazer
 Casual Office Blazer
 Elegant Blazer Look
 Tweed Blazer Jacket
 Women’s Blazer Trend
 Relaxed Fit Blazer
 Women’s Blazer Fashion
 Modern Women’s Blazer
 Blazer with Pockets
 Faux Leather Blazer
 Lightweight Blazer Jacket
 Blazer Jacket Style
 Workwear Women’s Blazer
 Double-breasted Blazer Jacket
 Long Sleeve Women’s Blazer
 Stylish Tweed Blazer
 Zipper Blazer for Women
 Casual Blazer Jackets
 Women’s Blazer Chic
 Classic Office Blazer
 Blazers for Women’s Wardrobe
 Blazer with Belt
 Slim Cut Blazer
 Women’s Black Blazer
 Modern Tailored Blazer
 Trendy Blazer Outfit
 Elegant Office Blazer
 Structured Blazer Jacket
 Cozy Blazer for Women
 Buttoned Blazer for Women
 Women’s Blazer with Pleats
 Chic Office Blazer
 Layered Women’s Blazer
 Minimalist Blazer Look
 Classic Style Blazer
 Elegant Blazer Dress
 Lightweight Work Blazer
 Fashionable Women’s Blazer
 Double Button Blazer
 Business Casual Blazer
 Slim Fit Blazer Jacket
 Structured Blazer Look
 Women’s Relaxed Blazer
 Stylish Women’s Blazer
 Blazer with Lapel
 Fitted Women’s Blazer
 Tweed Blazer Outfit
 Checked Blazer for Women
 Modern Work Blazer
 Classic Black Blazer
 Oversized Blazer Look
 Elegant Tweed Blazer
 Stylish Fitted Blazer
 Work Blazer Collection
 Lightweight Double-breasted Blazer
 Office Ready Blazer
 Single Button Blazer
 Printed Women’s Blazer
 Blazer for Smart Casual
 Blazer with Shoulder Pads
 Office Wear Blazers
 Fitted Blazer Jacket
 Classic Women’s Blazer
 Blazer with Ruffles
 Long Blazer Style
 Structured Tweed Blazer
 Professional Women’s Blazer
 Casual Blazer Outfit
 Women’s Business Blazer
 Slim Fit Office Blazer
 Checked Blazer Jacket
 Long Sleeve Blazer
 Chic Double-breasted Blazer
 Blazer for Date Night
 Office Blazer Style
"""

Pencil_Skirt_l=r"""
 Classic Pencil Skirt
 High-Waisted Pencil Skirt
 Slim Fit Pencil Skirt
 Office Pencil Skirt
 Sexy Pencil Skirt
 Formal Pencil Skirt
 Elegant Pencil Skirt
 Pencil Skirt Style
 Casual Pencil Skirt
 Black Pencil Skirt
 Denim Pencil Skirt
 Pencil Skirt Look
 A-line Pencil Skirt
 Printed Pencil Skirt
 Pleated Pencil Skirt
 Button-up Pencil Skirt
 Leather Pencil Skirt
 Pencil Skirt Dress
 Pencil Skirt Set
 Bodycon Pencil Skirt
 White Pencil Skirt
 Stretch Pencil Skirt
 Office Wear Pencil
 Chic Pencil Skirt
 Pencil Skirt Fashion
 Stylish Pencil Skirt
 Pencil Skirt Trend
 Summer Pencil Skirt
 Ruffled Pencil Skirt
 Pencil Skirt Combo
 Fitted Pencil Skirt
 Pencil Skirt Outfit
 Midi Pencil Skirt
 Back Slit Pencil Skirt
 Wool Pencil Skirt
 Fit-and-Flare Pencil
 Pencil Skirt Elegance
 Plaid Pencil Skirt
 Tweed Pencil Skirt
 Pencil Skirt Chic
 Wrap Pencil Skirt
 Button Detail Pencil
 Pencil Skirt Glam
 High-Rise Pencil Skirt
 Stretch Fit Pencil
 Pencil Skirt Classic
 Skirt with Pockets
 Pencil Skirt Trendy
 Comfy Pencil Skirt
 Pleated High-Waisted Skirt
 Simple Pencil Skirt
 Flared Pencil Skirt
 Rigid Pencil Skirt
 Modern Pencil Skirt
 Pencil Skirt Perfect
 Fitted High-Waisted Skirt
 Polka Dot Pencil
 Soft Pencil Skirt
 Stretchable Pencil Skirt
 Formal Wear Pencil
 Elegant Office Skirt
 Stretchy Pencil Skirt
 Pencil Skirt Glamour
 Tartan Pencil Skirt
 Colorblock Pencil Skirt
 Office Chic Pencil
 Knee-Length Pencil Skirt
 Sleek Pencil Skirt
 Pencil Skirt Dressy
 Stylish High-Waisted Skirt
 Pencil Skirt Lookbook
 Pencil Skirt Party
 Smart Pencil Skirt
 Faux Leather Pencil
 Slim Pencil Skirt
 Bold Pencil Skirt
 Tapered Pencil Skirt
 Plain Pencil Skirt
 Wide Waistband Pencil
 Vintage Pencil Skirt
 Lace Pencil Skirt
 Velvet Pencil Skirt
 Pencil Skirt Workwear
 Mini Pencil Skirt
 Asymmetrical Pencil Skirt
 Tight Fit Pencil Skirt
 Checkered Pencil Skirt
 Skirt with Belt
 Pencil Skirt Vibe
 Office Ready Pencil
 Fancy Pencil Skirt
 Ripped Pencil Skirt
 Knee Length Pencil
 Tied Pencil Skirt
 Casual Office Skirt
 Bold High-Waisted Skirt
 Statement Pencil Skirt
 Wide Waist Pencil
 Bright Pencil Skirt
 Front Slit Pencil
"""

Denim_Skirt_l=r"""
 Casual Denim Skirt
 High-Waisted Denim Skirt
 Classic Denim Skirt
 Flared Denim Skirt
 A-line Denim Skirt
 Stylish Denim Skirt
 Ripped Denim Skirt
 Mini Denim Skirt
 Button-front Denim Skirt
 Pleated Denim Skirt
 Vintage Denim Skirt
 Stretch Denim Skirt
 Skinny Denim Skirt
 Summer Denim Skirt
 Black Denim Skirt
 White Denim Skirt
 Blue Denim Skirt
 Skater Denim Skirt
 Printed Denim Skirt
 Denim Skirt Trend
 Belted Denim Skirt
 Distressed Denim Skirt
 Slim-fit Denim Skirt
 Denim Skirt Look
 Chic Denim Skirt
 Soft Denim Skirt
 Embellished Denim Skirt
 Denim Skirt Outfit
 Boho Denim Skirt
 Elegant Denim Skirt
 Ripped Hem Denim
 Long Denim Skirt
 Denim Skirt Style
 Denim Skirt Fashion
 Cute Denim Skirt
 Stretchy Denim Skirt
 Denim Skirt Set
 Colorful Denim Skirt
 Button-up Denim Skirt
 Relaxed Denim Skirt
 Slim Denim Skirt
 Modern Denim Skirt
 Flowy Denim Skirt
 Skirt with Denim
 Casual High-waisted Denim
 Raw Hem Denim
 Denim Skirt Flare
 Short Denim Skirt
 Button-down Denim Skirt
 Vintage Style Denim
 Denim Skirt Casual
 Classic Blue Denim
 Fringe Denim Skirt
 Patchwork Denim Skirt
 Denim Skirt Trendy
 Casual Button Denim
 Mid-rise Denim Skirt
 Ruffle Hem Denim
 Tattered Denim Skirt
 Comfy Denim Skirt
 Buttoned Denim Skirt
 Pencil Denim Skirt
 Denim Skirt Dress
 Flared A-line Denim
 Front Button Denim
 Trendy Denim Skirt
 Sexy Denim Skirt
 Buttoned-up Denim Skirt
 Loose Fit Denim
 Denim Skirt Glam
 Fitted Denim Skirt
 Simple Denim Skirt
 Maxi Denim Skirt
 Black High-Waisted Denim
 Relaxed Fit Denim
 Denim Skirt Chic
 Casual Mini Denim
 Stylish Ripped Denim
 High-Waist Denim Skirt
 Loose Denim Skirt
 Button Detail Denim
 Cool Denim Skirt
 Denim Skirt Appeal
 Full Denim Skirt
 Button Front Denim Skirt
 Light Wash Denim Skirt
 Dark Denim Skirt
 Skirt with Pockets
 Elastic Waist Denim Skirt
 Flared Hem Denim Skirt
 Mid-Length Denim Skirt
 High Rise Denim Skirt
 Embroidered Denim Skirt
 Fashionable Denim Skirt
 Classic Blue Denim Skirt
 Slim Fit Denim Skirt
 Comfortable Denim Skirt
 Ripped Front Denim Skirt
 Loose Fit Denim Skirt
 Wide Leg Denim Skirt
"""

Mini_Skirt_l=r"""
--Sexy Mini Skirt
--Casual Mini Skirt
--Chic Denim Skirt
--Elegant Mini Skirt
--Flirty Mini Skirt
--Trendy Mini Skirt
--High-Waisted Mini Skirt
--Ripped Denim Skirt
--Pleated Mini Skirt
--Floral Print Skirt
--Leather Mini Skirt
--Boho Mini Skirt
--A-line Mini Skirt
--Comfortable Mini Skirt
--Skater Mini Skirt
--Printed Mini Skirt
--Mini Skirt Set
--Mini Skirt Outfit
--Mini Skirt Chic
--Stylish Mini Skirt
--Simple Mini Skirt
--High-waist Denim Skirt
--Mini Skirt Dress
--Soft Mini Skirt
--Colorblock Mini Skirt
--Sexy Leather Skirt
--Casual Skater Skirt
--Button-front Mini Skirt
--Mini Skirt with Pockets
--Summer Mini Skirt
--Casual Summer Skirt
--Mini Skirt Style
--High-waist Skirt Trend
--Ruffled Mini Skirt
--Mini Skirt Look
--Fitted Mini Skirt
--Plaid Mini Skirt
--Mini Skirt Fashion
--Lace Detail Mini Skirt
--Bohemian Mini Skirt
--Mini Skirt Vibes
--Sleek Mini Skirt
--Distressed Mini Skirt
--Basic Mini Skirt
--Soft Denim Skirt
--Bold Mini Skirt
--Colorful Mini Skirt
--Skirt with Buttons
--Mini Skirt Trend
--Pleated Denim Skirt
--Summer Denim Mini
--Mini Skirt with Belt
--Vintage Mini Skirt
--Lace Mini Skirt
--Printed Denim Skirt
--Camo Mini Skirt
--Button-up Mini Skirt
--Bodycon Mini Skirt
--Soft Pleated Skirt
--Long-sleeve Mini Skirt
--Vintage Denim Skirt
--Cozy Mini Skirt
--Plaid Skater Skirt
--Polka Dot Mini Skirt
--Mini Skirt Summer
--Mini Skirt Trendy
--Mini Skirt Classic
--Boho Chic Mini Skirt
--Lace-up Mini Skirt
--Faded Denim Skirt
--Slim Fit Mini Skirt
--Wrap Mini Skirt
--Classic Denim Mini
--Stylish Pleated Skirt
--A-line Denim Skirt
--Black Mini Skirt
--Mini Skirt Casual
--Polka Dot Skirt
--Mini Skirt Party
--High-Waisted Skater Skirt
--Front Pocket Mini Skirt
--Soft Leather Skirt
--Retro Mini Skirt
--Fringed Mini Skirt
--Mini Skirt with Lace
--Floral A-line Skirt
--Ripped Mini Denim Skirt
--White Mini Skirt
--Stretch Mini Skirt
--Raw Hem Mini Skirt
--Tie Waist Mini Skirt
--Cute Mini Skirt
--Vintage Pleated Skirt
--Mini Skirt with Bow
--Pleated Mini Denim
--Fitted Pleated Skirt
--Cozy Denim Mini Skirt
--Summer Skater Skirt
--Button-down Mini Skirt
--High-Waist Skirt Look
"""

Mini_Dresses_l=r"""
 Women's mini dresses
 Summer mini dresses
 Casual mini dresses
 Party mini dresses
 Elegant mini dresses
 Sexy mini dresses
 Long sleeve mini dresses
 Sleeveless mini dresses
 Strapless mini dresses
 Off-shoulder mini dresses
 Cotton mini dresses
 Satin mini dresses
 Silk mini dresses
 Lace mini dresses
 Denim mini dresses
 Velvet mini dresses
 Chiffon mini dresses
 Knitted mini dresses
 Sequin mini dresses
 Leather mini dresses
 Wedding guest mini dresses
 Date night mini dresses
 Club mini dresses
 Cocktail mini dresses
 Beach mini dresses
 Vacation mini dresses
 Formal mini dresses
 Office mini dresses
 Graduation mini dresses
 Festival mini dresses
 Vintage mini dresses
 Boho mini dresses
 Chic mini dresses
 Y2K mini dresses
 Edgy mini dresses
 Minimalist mini dresses
 Glamorous mini dresses
 Street style mini dresses
 Preppy mini dresses
 Goth mini dresses
 Zara mini dresses
 H&M mini dresses
 Forever 21 mini dresses
 PrettyLittleThing mini dresses
 Shein mini dresses
 Revolve mini dresses
 ASOS mini dresses
 Fashion Nova mini dresses
 Boohoo mini dresses
 Urban Outfitters mini dresses
 Stretchy mini dresses
 Flowy mini dresses
 Bodycon mini dresses
 Wrap mini dresses
 Smocked mini dresses
 Ruffled mini dresses
 Tiered mini dresses
 A-line mini dresses
 Corset mini dresses
 Halter mini dresses
 Summer party mini dresses
 Winter mini dresses
 Spring mini dresses
 Fall mini dresses
 Birthday mini dresses
 Anniversary mini dresses
 Clubbing mini dresses
 Prom mini dresses
 Red carpet mini dresses
 New Year's Eve mini dresses
 Affordable mini dresses
 Cheap mini dresses
 Luxury mini dresses
 Designer mini dresses
 Budget-friendly mini dresses
 Expensive mini dresses
 High-end mini dresses
 Discounted mini dresses
 Best value mini dresses
 Trendy mini dresses under $50
 Best mini dresses for petites
 Best mini dresses for curvy figures
 Best mini dresses for tall women
 Best mini dresses for plus size
 Best mini dresses for hourglass body shape
 Best mini dresses for date night
 Best mini dresses for casual wear
 Best mini dresses for formal events
 Best mini dresses for summer vacation
 Best mini dresses for elegant looks
 Women's trendy mini dresses sale
 Sexy little black mini dresses
 Cute floral print mini dresses
 Comfortable mini dresses for everyday wear
 Fashion-forward mini dresses
 Lightweight mini dresses for hot weather
 Versatile mini dresses for all occasions
 Flattering mini dresses for all body types
 Must-have mini dresses for this season
 Hot new arrivals in mini dresses
"""

Unclassified_Skirt_l=r"""
 Women's unclassified skirts
 Stylish unclassified skirts
 Trendy unclassified skirts
 Elegant unclassified skirts
 Casual unclassified skirts
 Sexy unclassified skirts
 Chic unclassified skirts
 Unique unclassified skirts
 Fashionable unclassified skirts
 Affordable unclassified skirts
 Luxury unclassified skirts
 Comfortable unclassified skirts
 Designer unclassified skirts
 Plus size unclassified skirts
 Petite unclassified skirts
 High-waisted unclassified skirts
 Low-rise unclassified skirts
 Short unclassified skirts
 Long unclassified skirts
 Flowy unclassified skirts
 A-line unclassified skirts
 Pleated unclassified skirts
 Wrap unclassified skirts
 Ruffled unclassified skirts
 Tiered unclassified skirts
 Corset unclassified skirts
 Smocked unclassified skirts
 Ruched unclassified skirts
 Asymmetrical unclassified skirts
 Slit unclassified skirts
 High-low unclassified skirts
 Button-front unclassified skirts
 Side-tie unclassified skirts
 Mermaid unclassified skirts
 Pencil unclassified skirts
 Boho unclassified skirts
 Minimalist unclassified skirts
 Y2K unclassified skirts
 Gothic unclassified skirts
 Preppy unclassified skirts
 Street style unclassified skirts
 Formal unclassified skirts
 Casual chic unclassified skirts
 Satin unclassified skirts
 Lace unclassified skirts
 Silk unclassified skirts
 Velvet unclassified skirts
 Chiffon unclassified skirts
 Cotton unclassified skirts
 Denim unclassified skirts
 Mesh unclassified skirts
 Knitted unclassified skirts
 Tulle unclassified skirts
 Sequin unclassified skirts
 Leather unclassified skirts
 Floral unclassified skirts
 Striped unclassified skirts
 Polka dot unclassified skirts
 Color block unclassified skirts
 Printed unclassified skirts
 Embroidered unclassified skirts
 Beaded unclassified skirts
 Metallic unclassified skirts
 Monochrome unclassified skirts
 Pastel unclassified skirts
 Bright color unclassified skirts
 Dark color unclassified skirts
 Neutral tone unclassified skirts
 Earthy tone unclassified skirts
 Bold pattern unclassified skirts
 Soft fabric unclassified skirts
 Lightweight unclassified skirts
 Breathable unclassified skirts
 Stretchy unclassified skirts
 Elegant evening unclassified skirts
 Summer unclassified skirts
 Winter unclassified skirts
 Spring unclassified skirts
 Fall unclassified skirts
 Wedding guest unclassified skirts
 Date night unclassified skirts
 Party unclassified skirts
 Club unclassified skirts
 Anniversary unclassified skirts
 Engagement unclassified skirts
 Graduation unclassified skirts
 Cocktail unclassified skirts
 Vacation unclassified skirts
 Beach unclassified skirts
 Office unclassified skirts
 Travel unclassified skirts
 Festival unclassified skirts
 Holiday unclassified skirts
 Everyday wear unclassified skirts
 Lounge unclassified skirts
 Trendy new unclassified skirts
 Popular unclassified skirts
 Best-selling unclassified skirts
 High-end unclassified skirts
 Discounted unclassified skirts
"""

Party_Dress_l=r"""
 Hot new arrivals in party dresses
 Women's party dresses
 Men's party outfits
 Girls' party dresses
 Plus size party dresses
 Petite party dresses
 Maternity party dresses
 Sexy party dresses
 Elegant party dresses
 Modest party dresses
 Vintage party dresses
 Satin party dresses
 Silk party dresses
 Velvet party dresses
 Chiffon party dresses
 Lace party dresses
 Sequin party dresses
 Cotton party dresses
 Leather party dresses
 Tulle party dresses
 Knitted party dresses
 Wedding guest party dresses
 Birthday party dresses
 Cocktail party dresses
 Club party dresses
 Dinner party dresses
 Holiday party dresses
 Graduation party dresses
 Engagement party dresses
 New Year's Eve party dresses
 Bachelorette party dresses
 Boho party dresses
 Chic party dresses
 Y2K party dresses
 Edgy party dresses
 Minimalist party dresses
 Glamorous party dresses
 Street style party dresses
 Preppy party dresses
 Gothic party dresses
 Classic party dresses
 Zara party dresses
 H&M party dresses
 Forever 21 party dresses
 PrettyLittleThing party dresses
 Shein party dresses
 Revolve party dresses
 ASOS party dresses
 Fashion Nova party dresses
 Boohoo party dresses
 Urban Outfitters party dresses
 Stretchy party dresses
 Flowy party dresses
 Bodycon party dresses
 Wrap party dresses
 Smocked party dresses
 Ruffled party dresses
 Tiered party dresses
 A-line party dresses
 Corset party dresses
 Halter party dresses
 Christmas party dresses
 Office party dresses
 Summer party dresses
 Winter party dresses
 Spring party dresses
 Fall party dresses
 Outdoor party dresses
 Garden party dresses
 Formal party dresses
 Casual party dresses
 Affordable party dresses
 Cheap party dresses
 Luxury party dresses
 Designer party dresses
 Budget-friendly party dresses
 Expensive party dresses
 High-end party dresses
 Discounted party dresses
 Best value party dresses
 Trendy party dresses under $50
 Best party dresses for petites
 Best party dresses for curvy figures
 Best party dresses for tall women
 Best party dresses for plus size
 Best party dresses for hourglass body shape
 Best party dresses for date night
 Best party dresses for cocktail parties
 Best party dresses for dancing
 Best party dresses for wedding guests
 Best party dresses for formal events
 Women's trendy party dresses sale
 Sexy little black party dresses
 Cute floral print party dresses
 Comfortable party dresses for all-night wear
 Fashion-forward party dresses
 Lightweight party dresses for summer
 Versatile party dresses for any occasion
 Flattering party dresses for all body types
 Must-have party dresses for this season
"""

Wedding_Dress_l=r"""
 Elegant Bridal Gown
 Lace Wedding Dress
 Satin Bridal Gown
 Romantic Lace Dress
 Chic Wedding Gown
 A-line Bridal Dress
 Glamorous Wedding Dress
 Off-shoulder Wedding Gown
 Vintage Lace Dress
 Modern Bridal Gown
 Sleeveless Wedding Dress
 Mermaid Wedding Gown
 Floral Lace Wedding
 Elegant Satin Dress
 Boho Wedding Gown
 Lace Sleeveless Dress
 Princess Wedding Dress
 White Lace Gown
 Soft Satin Bridal
 Long Sleeve Gown
 Sparkling Wedding Dress
 Classic Bridal Gown
 Simple Wedding Dress
 Luxury Lace Gown
 Sexy Wedding Dress
 Modern Wedding Gown
 Full Skirt Wedding
 Sparkle Bridal Dress
 Empire Waist Gown
 Tiered Wedding Dress
 Sexy Lace Gown
 Simple Satin Gown
 Floral Wedding Gown
 Strapless Bridal Dress
 Beaded Wedding Gown
 Sheer Wedding Dress
 Off-shoulder Gown
 Open Back Dress
 Mermaid Style Gown
 Elegant Lace Gown
 Boho Chic Gown
 Formal Wedding Dress
 Modern Lace Gown
 Classic Satin Gown
 Lace V-neck Dress
 Ball Gown Wedding
 Wedding Dress Set
 Illusion Neckline Gown
 Lace A-line Dress
 Ruffled Wedding Dress
 Sexy Satin Gown
 Glitter Wedding Dress
 Princess Bridal Dress
 Silk Wedding Gown
 Lace Train Dress
 Vintage Wedding Gown
 Chic Lace Dress
 Wedding Dress Style
 Empire Waist Dress
 Strapless Wedding Gown
 Wedding Gown Set
 Soft Lace Gown
 Full Length Gown
 Luxury Wedding Dress
 Sleeveless Bridal Gown
 Ruffle Wedding Gown
 Classic Bridal Dress
 A-line Wedding Gown
 Timeless Wedding Dress
 Beautiful Lace Gown
 Beaded Bridal Gown
 Off-shoulder Bridal Dress
 Illusion Lace Gown
 Simple Wedding Gown
 Lace Boho Dress
 Romantic Wedding Dress
 Floral Bridal Gown
 Vintage Style Dress
 Mermaid Lace Gown
 Elegant A-line Gown
 Satin Wedding Dress
 Classic Lace Gown
 Off-shoulder Bridal Gown
 Beaded Lace Wedding
 Embroidered Wedding Dress
 Sparkling Bridal Gown
 Lace Back Wedding
 Soft Wedding Gown
 Sleek Wedding Dress
 Chic Bridal Gown
 Strapless Lace Dress
 Crystal Wedding Dress
 Full Skirt Gown
 Lace Wedding Gown
 Silk Bridal Dress
 Short Wedding Gown
 Beautiful Bridal Gown
 Wedding Dress Long
 Romantic Satin Dress
 Satin Lace Gown
"""

Floral_Dress_l=r"""
 Women's floral dresses
 Girls' floral dresses
 Plus size floral dresses
 Petite floral dresses
 Maternity floral dresses
 Short floral dresses
 Long floral dresses
 Maxi floral dresses
 Midi floral dresses
 Mini floral dresses
 Cotton floral dresses
 Chiffon floral dresses
 Satin floral dresses
 Silk floral dresses
 Lace floral dresses
 Linen floral dresses
 Velvet floral dresses
 Organza floral dresses
 Knitted floral dresses
 Tulle floral dresses
 Casual floral dresses
 Elegant floral dresses
 Summer floral dresses
 Spring floral dresses
 Beach floral dresses
 Party floral dresses
 Wedding guest floral dresses
 Formal floral dresses
 Office floral dresses
 Vacation floral dresses
 Vintage floral dresses
 Boho floral dresses
 Chic floral dresses
 Romantic floral dresses
 Edgy floral dresses
 Minimalist floral dresses
 Y2K floral dresses
 Cottagecore floral dresses
 Preppy floral dresses
 Retro floral dresses
 Zara floral dresses
 H&M floral dresses
 Forever 21 floral dresses
 PrettyLittleThing floral dresses
 Shein floral dresses
 Revolve floral dresses
 ASOS floral dresses
 Fashion Nova floral dresses
 Boohoo floral dresses
 Urban Outfitters floral dresses
 Stretchy floral dresses
 Flowy floral dresses
 Bodycon floral dresses
 Wrap floral dresses
 Smocked floral dresses
 Ruffled floral dresses
 Tiered floral dresses
 A-line floral dresses
 Corset floral dresses
 Halter floral dresses
 Date night floral dresses
 Birthday floral dresses
 Garden party floral dresses
 Outdoor floral dresses
 Wedding floral dresses
 Anniversary floral dresses
 Graduation floral dresses
 Brunch floral dresses
 Cocktail floral dresses
 New Year's Eve floral dresses
 Affordable floral dresses
 Cheap floral dresses
 Luxury floral dresses
 Designer floral dresses
 Budget-friendly floral dresses
 Expensive floral dresses
 High-end floral dresses
 Discounted floral dresses
 Floral dresses under $50
 Floral dresses under $100
 Best floral dresses for petites
 Best floral dresses for curvy figures
 Best floral dresses for tall women
 Best floral dresses for plus size
 Best floral dresses for hourglass body shape
 Best floral dresses for beach vacations
 Best floral dresses for outdoor weddings
 Best floral dresses for casual outings
 Best floral dresses for work
 Best floral dresses for elegant looks
 Women's trendy floral dresses sale
 Sexy floral print dresses
 Cute floral print summer dresses
 Comfortable floral dresses for everyday wear
 Fashion-forward floral dresses
 Lightweight floral dresses for hot weather
 Versatile floral dresses for all occasions
 Flattering floral dresses for all body types
 Must-have floral dresses for this season
 Hot new arrivals in floral dresses
"""

Shirt_Dress_l=r"""
 Casual Shirt Dress
 Elegant Shirt Dress
 Stylish Shirt Dress
 Button-up Shirt Dress
 Comfortable Shirt Dress
 Trendy Shirt Dress
 Classic Shirt Dress
 Loose Shirt Dress
 Casual Button Shirt
 Chic Shirt Dress
 Shirt Dress Look
 Summer Shirt Dress
 Long Sleeve Shirt
 Shirt Dress Style
 Flowy Shirt Dress
 Linen Shirt Dress
 Short Shirt Dress
 Oversized Shirt Dress
 Tartan Shirt Dress
 Denim Shirt Dress
 Shirt Dress Trend
 Cotton Shirt Dress
 Pleated Shirt Dress
 Midi Shirt Dress
 Shirt Dress Fashion
 Belted Shirt Dress
 Button-down Shirt Dress
 Boho Shirt Dress
 Printed Shirt Dress
 White Shirt Dress
 Blue Shirt Dress
 Polka Dot Shirt
 Sleeveless Shirt Dress
 Relaxed Shirt Dress
 Floral Shirt Dress
 Simple Shirt Dress
 Shirt Dress Chic
 Plaid Shirt Dress
 Ruffled Shirt Dress
 A-line Shirt Dress
 Modern Shirt Dress
 Comfy Shirt Dress
 Office Shirt Dress
 Wrap Shirt Dress
 Shirt Dress Combo
 Fashion Shirt Dress
 Flared Shirt Dress
 Vintage Shirt Dress
 Soft Shirt Dress
 Formal Shirt Dress
 Cute Shirt Dress
 Silk Shirt Dress
 Shift Shirt Dress
 Casual Dress Shirt
 Tied Shirt Dress
 Stretch Shirt Dress
 Sexy Shirt Dress
 Dress Shirt Chic
 V-neck Shirt Dress
 Long Shirt Dress
 White Linen Shirt
 Black Shirt Dress
 Stylish Button Shirt
 Day Shirt Dress
 Relaxed Fit Shirt
 Shirt Dress Party
 Formal Shirt Gown
 Button Front Shirt
 Elegant Shirt Gown
 Shirt Dress Glam
 Soft Cotton Shirt
 Modern Button Shirt
 Printed Button Shirt
 Classic Button Shirt
 Light Shirt Dress
 Classic Shirt Gown
 Fashionable Shirt Dress
 Striped Shirt Dress
 Button Detail Shirt
 Layered Shirt Dress
 Relaxed Shirt Gown
 Basic Shirt Dress
 Pleated Shirt Gown
 Belted Button Dress
 Sexy Shirt Gown
 Tartan Shirt Gown
 Shirt Dress Wrap
 Feminine Shirt Dress
 Casual Fit Shirt
 High-Waisted Shirt Dress
 Short Sleeve Shirt Dress
 Mini Shirt Dress
 Long Sleeve Shirt Dress
 Shirt Dress Outfit
 Elegant Button Shirt
 Shirt Dress Casual
 Satin Shirt Dress
 Fit-and-Flare Shirt Dress
 Lace Shirt Dress
 Bohemian Shirt Dress
"""

Pullovers_l=r"""
 Cozy Women’s Pullovers
 Casual Pullover Sweater
 Stylish Pullover Tops
 Warm Pullover Sweatshirt
 Classic Women’s Pullover
 Elegant Pullover Sweater
 Comfortable Pullover Sweatshirt
 Trendy Pullover Tops
 Soft Pullover Sweater
 Pullover Knit Sweater
 Relaxed Fit Pullover
 Pullover for Women
 Long Sleeve Pullover
 Fitted Pullover Sweater
 Casual Pullover Top
 Lightweight Pullover Sweater
 Pullover Sweater Fashion
 Women’s Pullover Knit
 Cozy Knit Pullover
 Warm Pullover Style
 Oversized Pullover Sweater
 Comfy Pullover Sweater
 Pullover Sweater Chic
 Pullover Knit Top
 Ribbed Pullover Sweater
 Women’s Classic Pullover
 Pullover Hoodie Sweater
 Casual Knit Pullover
 Stylish Pullover Sweater
 Pullover for Cold Weather
 Soft Knit Pullover
 Elegant Pullover Design
 Women’s Pullover Fashion
 Simple Pullover Sweater
 Pullover Sweater Trend
 Printed Pullover Sweater
 Cozy Winter Pullover
 Loose Fit Pullover
 Colorful Pullover Sweater
 Knit Pullover for Women
 Layered Pullover Sweater
 Lightweight Pullover Top
 Pullover Sweatshirt Style
 Pullover Sweater Look
 Pullover with Pattern
 Pullover Sweater with Pockets
 Warm Pullover Knit
 Vintage Pullover Sweater
 Pullover Sweater Collection
 Women’s Ribbed Pullover
 Everyday Pullover Sweater
 Relaxed Pullover Sweater
 Pullover Sweater Outfit
 Casual Wear Pullover
 Soft Wool Pullover
 High-neck Pullover Sweater
 Pullover with Zipper
 Slim Fit Pullover
 Pullover Sweater for Work
 Stylish Knit Pullover
 Printed Women’s Pullover
 Pullover Sweater with Design
 Pullover Tunic Sweater
 Oversized Knit Pullover
 Pullover with Button Detail
 Chunky Pullover Sweater
 Classic Pullover Sweater
 Warm Knit Pullover
 Elegant Women’s Pullover
 Fashionable Pullover Sweater
 Basic Pullover Sweater
 Cozy Wool Pullover
 Casual Knit Sweater
 Women’s Oversized Pullover
 Sleek Pullover Sweater
 Trendy Knit Pullover
 Colorblock Pullover Sweater
 Plain Pullover Sweater
 Loose Pullover Sweater
 Pullover Sweater Vibe
 Pullover for Layering
 Women’s Classic Sweater
 Warm Pullover for Fall
 Soft Women’s Pullover
 Comfy Wool Pullover
 Knit Pullover Sweater
 Pullover Sweater with Hood
 Basic Knit Pullover
 Women’s Sweater Pullover
 Casual Sweater Pullover
 Fuzzy Pullover Sweater
 Trendy Pullover Sweater
 Pullover with Ribbed Detail
 Elegant Knit Pullover
 Button-up Pullover Sweater
 Everyday Pullover Style
 Pullover Sweater for Winter
 Stylish Pullover Outfit
 Pullover Sweater Lookbook
 Women’s Pullover Hoodie
"""

Suspender_Dress_l=r"""
 Casual Suspender Dress
 Sexy Suspender Dress
 Trendy Suspender Dress
 Elegant Suspender Dress
 Suspender Dress Chic
 Cute Suspender Dress
 Casual Strap Dress
 Boho Suspender Dress
 Sleeveless Suspender Dress
 Summer Suspender Dress
 Sexy Strap Dress
 Vintage Suspender Dress
 High-Waisted Suspender Dress
 Flared Suspender Dress
 Buttoned Suspender Dress
 Mini Suspender Dress
 Suspender Dress Style
 Loose Fit Suspender
 Skater Suspender Dress
 Suspender Dress Fashion
 A-line Suspender Dress
 Floral Suspender Dress
 Chic Suspender Dress
 Suspender Dress Outfit
 Off-shoulder Suspender
 Ruffled Suspender Dress
 Suspender Dress Vibe
 Strap Detail Suspender
 Elegant Strap Dress
 Polka Dot Suspender
 Romantic Suspender Dress
 Suspender Dress Look
 Comfortable Suspender Dress
 Playful Suspender Dress
 Suspender Dress Glam
 Vintage Strap Dress
 Knit Suspender Dress
 Faux Leather Suspender
 Suspender Dress Trend
 Button-up Suspender Dress
 Suspender Dress Set
 Lace Suspender Dress
 Button Detail Suspender
 Office Suspender Dress
 Statement Suspender Dress
 Summer Strap Dress
 Bodycon Suspender Dress
 Backless Suspender Dress
 Modern Suspender Dress
 Ruffle Strap Suspender
 Fun Suspender Dress
 Sleeveless Strap Dress
 Chic Suspender Look
 Sweet Suspender Dress
 Street Style Suspender
 Suspender Dress Appeal
 Suspender Dress Detail
 Warm Suspender Dress
 Suspender Dress Holiday
 Skirted Suspender Dress
 Strap Dress Style
 Cool Suspender Dress
 Adjustable Strap Dress
 Elegant Suspender Design
 Party Suspender Dress
 Suspender Dress Lookbook
 Soft Suspender Dress
 Casual Day Suspender
 Bohemian Suspender Dress
 Suspender Dress with Pockets
 Relaxed Suspender Dress
 Colorful Suspender Dress
 Chic Strap Dress
 Suspender Dress Trendy
 V-neck Suspender Dress
 Fitted Suspender Dress
 Retro Suspender Dress
 Suspender Dress Summer
 Suspender Dress Layered
 Stylish Suspender Dress
 Classy Suspender Dress
 Strap-up Suspender Dress
 Feminine Suspender Dress
 Lace-up Suspender Dress
 Cool Suspender Look
 Suspender Dress Vintage
 Strappy Suspender Dress
 Fun Summer Suspender
 Floral Strap Dress
 Suspender Dress Ruffle
 Soft Fabric Suspender
 Suspender Dress Party
 Unique Suspender Dress
 Casual Wear Suspender
 Pleated Suspender Dress
 Short Suspender Dress
 Layered Suspender Dress
 Lace Suspender Design
 Skirt Suspender Dress
 Adjustable Suspender Dress
"""

Maxi_Skirt_l=r"""
 Elegant Maxi Skirt
 Casual Maxi Skirt
 Chic Maxi Skirt
 Boho Maxi Skirt
 Floral Maxi Skirt
 Pleated Maxi Skirt
 A-line Maxi Skirt
 High-Waisted Maxi Skirt
 Ruffled Maxi Skirt
 Satin Maxi Skirt
 Printed Maxi Skirt
 Summer Maxi Skirt
 Maxi Skirt Set
 Comfortable Maxi Skirt
 Trendy Maxi Skirt
 Maxi Skirt Outfit
 Soft Maxi Skirt
 Black Maxi Skirt
 Flowing Maxi Skirt
 Stylish Maxi Skirt
 Midi Maxi Skirt
 Vintage Maxi Skirt
 Lace Maxi Skirt
 Bohemian Maxi Skirt
 Tulle Maxi Skirt
 Silk Maxi Skirt
 Cozy Maxi Skirt
 Button-front Maxi Skirt
 Maxi Skirt Dress
 Button-up Maxi Skirt
 Maxi Skirt Chic
 Denim Maxi Skirt
 Pleated A-line Skirt
 Printed A-line Maxi
 Skater Maxi Skirt
 Formal Maxi Skirt
 Casual Long Skirt
 Ruffle Maxi Skirt
 Maxi Skirt Fashion
 Long Boho Skirt
 Front Slit Maxi
 Elegant Maxi Look
 Cotton Maxi Skirt
 Slim-fit Maxi Skirt
 Embroidered Maxi Skirt
 Tartan Maxi Skirt
 Casual Maxi Outfit
 Maxi Skirt Trend
 Midi Maxi Outfit
 Floral A-line Skirt
 Maxi Skirt Style
 Sexy Maxi Skirt
 Wrap Maxi Skirt
 Plaid Maxi Skirt
 Knit Maxi Skirt
 Stretch Maxi Skirt
 V-neck Maxi Skirt
 Front Pocket Maxi
 Maxi Skirt Party
 Summer Beach Maxi
 Soft Pleated Maxi
 Maxi Skirt Look
 Maxi Skirt Glam
 Boho Chic Maxi
 Soft Flow Maxi
 High-Waist Maxi Skirt
 Printed Long Skirt
 Maxi Skirt Classic
 Long Floral Skirt
 Formal Maxi Outfit
 Maxi Skirt Casual
 Summer Floral Maxi
 Skirt with Slits
 Elegant Long Skirt
 Maxi Skirt Trendy
 Chic Maxi Dress
 Soft Ruffled Maxi
 Button-down Maxi Skirt
 Sleek Maxi Skirt
 Comfortable Long Skirt
 Cozy Maxi Dress
 Maxi Skirt Collection
 Tulle Layered Maxi
 Bold Maxi Skirt
 High-Low Maxi Skirt
 Fitted Maxi Skirt
 Layered Maxi Skirt
 Soft Maxi Dress
 Front Slit Skirt
 Lace Detail Maxi
 Full Maxi Skirt
 Flowing Boho Skirt
 Embellished Maxi Skirt
 Pleated Floral Maxi
 Comfortable Maxi Look
 Colorful Maxi Skirt
 Sexy Long Skirt
 Ruffle Long Maxi
 Flowy Maxi Skirt
 Velvet Maxi Skirt
"""

Midi_Skirt_l=r"""
 Elegant Midi Skirt
 Casual Midi Skirt
 Chic Midi Skirt
 Stylish Midi Skirt
 Flowy Midi Skirt
 High-Waisted Midi Skirt
 Pleated Midi Skirt
 A-line Midi Skirt
 Boho Midi Skirt
 Denim Midi Skirt
 Floral Midi Skirt
 Satin Midi Skirt
 Summer Midi Skirt
 Ruffled Midi Skirt
 Button-front Midi Skirt
 Midi Skirt Set
 Midi Skirt Outfit
 Midi Skirt Chic
 Trendy Midi Skirt
 Soft Midi Skirt
 Midi Skirt Look
 Polka Dot Midi
 Printed Midi Skirt
 Black Midi Skirt
 Midi Skirt Fashion
 Pleated A-line Skirt
 Ruffled Floral Skirt
 Formal Midi Skirt
 Midi Skirt Style
 Wrap Midi Skirt
 Midi Skirt Trend
 Lace Midi Skirt
 Vintage Midi Skirt
 Soft Denim Midi
 Sexy Midi Skirt
 Elegant A-line Skirt
 Midi Skirt Party
 Knit Midi Skirt
 Winter Midi Skirt
 Elegant Satin Skirt
 Structured Midi Skirt
 Bohemian Midi Skirt
 Cozy Midi Skirt
 Long Midi Skirt
 Plain Midi Skirt
 Tulle Midi Skirt
 Bodycon Midi Skirt
 Slim Midi Skirt
 Casual A-line Skirt
 Midi Skirt Dress
 Cotton Midi Skirt
 Tartan Midi Skirt
 Pleated Satin Skirt
 Maxi Length Midi
 Midi Skirt with Pockets
 Fitted Midi Skirt
 Casual Midi Outfit
 Floral A-line Skirt
 Ribbed Midi Skirt
 Button-down Midi Skirt
 Classic Midi Skirt
 Soft A-line Skirt
 Ruffled Skirt Midi
 Sporty Midi Skirt
 Elegant Midi Dress
 Boho Chic Midi
 Stylish Pleated Skirt
 Silk Midi Skirt
 Printed Midi Outfit
 Midi Skirt Blouse
 Tulle A-line Skirt
 Printed Satin Midi
 Casual Midi Look
 Slim Fit Midi
 Front Button Midi
 Midi Skirt Trendy
 Elegant Midi Look
 Vintage Printed Skirt
 Midi Skirt Print
 Soft Pleated Midi
 Lace Trim Midi
 Fashion Midi Skirt
 Warm Midi Skirt
 Everyday Midi Skirt
 Bright Midi Skirt
 Lace-up Midi Skirt
 Winter Midi Outfit
 Embroidered Midi Skirt
 Pleated Floral Midi
 Soft Wool Midi
 Wraparound Midi Skirt
 Midi Skirt Casual
 Flared Midi Skirt
 Button Midi Skirt
 Trendy Midi Look
 Printed Floral Midi
 Wool Midi Skirt
 Classic A-line Skirt
 Cozy Midi Dress
 Skater Midi Skirt
"""

Womens_Jackets_l=r"""
 Women's winter jackets
 Women's summer jackets
 Women's lightweight jackets
 Women's waterproof jackets
 Women's casual jackets
 Women's warm jackets
 Women's trendy jackets
 Women's stylish jackets
 Women's long jackets
 Women's short jackets
 Women's denim jackets
 Women's leather jackets
 Women's wool jackets
 Women's fleece jackets
 Women's cotton jackets
 Women's quilted jackets
 Women's suede jackets
 Women's puffer jackets
 Women's polyester jackets
 Women's softshell jackets
 Women's hiking jackets
 Women's running jackets
 Women's ski jackets
 Women's cycling jackets
 Women's gym jackets
 Women's travel jackets
 Women's camping jackets
 Women's work jackets
 Women's office jackets
 Women's motorcycle jackets
 Women's fall jackets
 Women's spring jackets
 Women's winter puffer jackets
 Women's lightweight summer jackets
 Women's transitional jackets
 Women's autumn coats and jackets
 Women's cool weather jackets
 Women's winter-ready jackets
 Women's thermal jackets
 Women's all-season jackets
 Women's vintage jackets
 Women's oversized jackets
 Women's cropped jackets
 Women's fitted jackets
 Women's boho jackets
 Women's minimalist jackets
 Women's edgy jackets
 Women's elegant jackets
 Women's military-style jackets
 Women's sporty jackets
 Women's Nike jackets
 Women's Adidas jackets
 Women's Columbia jackets
 Women's North Face jackets
 Women's Patagonia jackets
 Women's Canada Goose jackets
 Women's Zara jackets
 Women's H&M jackets
 Women's Levi’s jackets
 Women's Gucci jackets
 Women's windproof jackets
 Women's insulated jackets
 Women's breathable jackets
 Women's UV protection jackets
 Women's reversible jackets
 Women's packable jackets
 Women's heated jackets
 Women's hooded jackets
 Women's reflective jackets
 Women's lined jackets
 Women's formal jackets
 Women's evening jackets
 Women's party jackets
 Women's streetwear jackets
 Women's weekend jackets
 Women's business casual jackets
 Women's date night jackets
 Women's wedding guest jackets
 Women's college jackets
 Women's travel-friendly jackets
 Women's affordable jackets
 Women's luxury jackets
 Women's budget jackets
 Women's premium jackets
 Women's high-end jackets
 Women's designer jackets
 Women's cheap jackets
 Women's best value jackets
 Women's mid-range jackets
 Women's discounted jackets
 Best women's jackets for winter
 Best women's jackets for rain
 Best women's jackets for layering
 Women's best-selling jackets
 Women's fashion jackets sale
 Women's commuter jackets
 Women's eco-friendly jackets
 Women's smart jackets
 Women's versatile jackets
 Women's must-have jackets
"""

Midi_Dresses_l=r"""
 Women's midi dresses
 Summer midi dresses
 Casual midi dresses
 Party midi dresses
 Elegant midi dresses
 Sexy midi dresses
 Long sleeve midi dresses
 Sleeveless midi dresses
 Strapless midi dresses
 Off-shoulder midi dresses
 Cotton midi dresses
 Satin midi dresses
 Silk midi dresses
 Lace midi dresses
 Denim midi dresses
 Velvet midi dresses
 Chiffon midi dresses
 Knitted midi dresses
 Sequin midi dresses
 Leather midi dresses
 Wedding guest midi dresses
 Date night midi dresses
 Cocktail midi dresses
 Beach midi dresses
 Vacation midi dresses
 Formal midi dresses
 Office midi dresses
 Graduation midi dresses
 Festival midi dresses
 Holiday midi dresses
 Vintage midi dresses
 Boho midi dresses
 Chic midi dresses
 Y2K midi dresses
 Edgy midi dresses
 Minimalist midi dresses
 Glamorous midi dresses
 Street style midi dresses
 Preppy midi dresses
 Goth midi dresses
 Zara midi dresses
 H&M midi dresses
 Forever 21 midi dresses
 PrettyLittleThing midi dresses
 Shein midi dresses
 Revolve midi dresses
 ASOS midi dresses
 Fashion Nova midi dresses
 Boohoo midi dresses
 Urban Outfitters midi dresses
 Stretchy midi dresses
 Flowy midi dresses
 Bodycon midi dresses
 Wrap midi dresses
 Smocked midi dresses
 Ruffled midi dresses
 Tiered midi dresses
 A-line midi dresses
 Corset midi dresses
 Halter midi dresses
 Summer party midi dresses
 Winter midi dresses
 Spring midi dresses
 Fall midi dresses
 Birthday midi dresses
 Anniversary midi dresses
 Clubbing midi dresses
 Prom midi dresses
 Red carpet midi dresses
 New Year's Eve midi dresses
 Affordable midi dresses
 Cheap midi dresses
 Luxury midi dresses
 Designer midi dresses
 Budget-friendly midi dresses
 Expensive midi dresses
 High-end midi dresses
 Discounted midi dresses
 Best value midi dresses
 Trendy midi dresses under $50
 Best midi dresses for petites
 Best midi dresses for curvy figures
 Best midi dresses for tall women
 Best midi dresses for plus size
 Best midi dresses for hourglass body shape
 Best midi dresses for date night
 Best midi dresses for casual wear
 Best midi dresses for formal events
 Best midi dresses for summer vacation
 Best midi dresses for elegant looks
 Women's trendy midi dresses sale
 Sexy little black midi dresses
 Cute floral print midi dresses
 Comfortable midi dresses for everyday wear
 Fashion-forward midi dresses
 Lightweight midi dresses for hot weather
 Versatile midi dresses for all occasions
 Flattering midi dresses for all body types
 Must-have midi dresses for this season
 Hot new arrivals in midi dresses
"""

Unclassified_Dresses_l=r"""
 Women's unclassified dresses
 Stylish unclassified dresses
 Trendy unclassified dresses
 Elegant unclassified dresses
 Casual unclassified dresses
 Sexy unclassified dresses
 Chic unclassified dresses
 Unique unclassified dresses
 Fashionable unclassified dresses
 Affordable unclassified dresses
 Luxury unclassified dresses
 Comfortable unclassified dresses
 Designer unclassified dresses
 Plus size unclassified dresses
 Petite unclassified dresses
 Sleeveless unclassified dresses
 Long sleeve unclassified dresses
 Short unclassified dresses
 Long unclassified dresses
 Flowy unclassified dresses
 A-line unclassified dresses
 Bodycon unclassified dresses
 Wrap unclassified dresses
 Ruffled unclassified dresses
 Tiered unclassified dresses
 Corset unclassified dresses
 Smocked unclassified dresses
 Ruched unclassified dresses
 Halter unclassified dresses
 Off-shoulder unclassified dresses
 One-shoulder unclassified dresses
 High-low unclassified dresses
 Backless unclassified dresses
 Open-back unclassified dresses
 Vintage unclassified dresses
 Boho unclassified dresses
 Minimalist unclassified dresses
 Y2K unclassified dresses
 Gothic unclassified dresses
 Preppy unclassified dresses
 Street style unclassified dresses
 Formal unclassified dresses
 Casual chic unclassified dresses
 Satin unclassified dresses
 Lace unclassified dresses
 Silk unclassified dresses
 Velvet unclassified dresses
 Chiffon unclassified dresses
 Cotton unclassified dresses
 Denim unclassified dresses
 Mesh unclassified dresses
 Knitted unclassified dresses
 Tulle unclassified dresses
 Sequin unclassified dresses
 Floral unclassified dresses
 Striped unclassified dresses
 Polka dot unclassified dresses
 Color block unclassified dresses
 Printed unclassified dresses
 Embroidered unclassified dresses
 Beaded unclassified dresses
 Metallic unclassified dresses
 Monochrome unclassified dresses
 Pastel unclassified dresses
 Bright color unclassified dresses
 Dark color unclassified dresses
 Neutral tone unclassified dresses
 Earthy tone unclassified dresses
 Bold pattern unclassified dresses
 Soft fabric unclassified dresses
 Lightweight unclassified dresses
 Breathable unclassified dresses
 Stretchy unclassified dresses
 Elegant evening unclassified dresses
 Summer unclassified dresses
 Winter unclassified dresses
 Spring unclassified dresses
 Fall unclassified dresses
 Wedding guest unclassified dresses
 Date night unclassified dresses
 Party unclassified dresses
 Club unclassified dresses
 Anniversary unclassified dresses
 Engagement unclassified dresses
 Graduation unclassified dresses
 Cocktail unclassified dresses
 Vacation unclassified dresses
 Beach unclassified dresses
 Office unclassified dresses
 Travel unclassified dresses
 Festival unclassified dresses
 Holiday unclassified dresses
 Everyday wear unclassified dresses
 Lounge unclassified dresses
 Trendy new unclassified dresses
 Popular unclassified dresses
 Best-selling unclassified dresses
 High-end unclassified dresses
 Budget-friendly unclassified dresses
 Discounted unclassified dresses
"""

Robe_Gown_Sets_l=r"""
 Elegant Satin Robe
 Luxurious Bridal Gown
 Soft Velvet Robe
 Cozy Cotton Gown
 Lace Trim Robe
 Silk Wedding Gown
 Comfy Satin Set
 Bridal Lingerie Robe
 Long Sleeve Gown
 Plush Robe Set
 Floral Lace Robe
 Sleeveless Satin Gown
 Romantic Bridal Set
 Satin Evening Gown
 Elegant Gown Robe
 Spa Robe Set
 Chic Satin Robe
 Sleeveless Bridal Gown
 Cozy Evening Gown
 Long Satin Robe
 Satin Kimono Gown
 Bridal Robe Set
 Soft Silk Robe
 Luxe Velvet Gown
 Romantic Lace Set
 Satin Lace Robe
 Bridal Satin Gown
 Cozy Winter Robe
 Elegant Lace Gown
 Silk Robe Set
 Lace Satin Gown
 Spa Luxury Robe
 Soft Cotton Gown
 Satin Bathrobe Set
 Comfy Night Gown
 Silk Kimono Robe
 Boho Style Robe
 Luxe Satin Gown
 Elegant Satin Set
 Silk Lingerie Robe
 Floral Gown Set
 Long Satin Gown
 Plush Bathrobe Set
 Warm Robe Gown
 Bridal Satin Set
 Silk Lace Robe
 Luxury Satin Gown
 Soft Lace Robe
 Cozy Satin Gown
 Glamorous Robe Set
 Sleeveless Lace Robe
 Comfy Robe Gown
 Satin Spa Gown
 Soft Bridal Robe
 Bridal Night Robe
 Silk Satin Gown
 Cozy Lace Robe
 Long Kimono Robe
 Cozy Bridal Set
 Elegant Robe Gown
 Chic Bridal Gown
 Satin Lingerie Set
 Soft Satin Robe
 Velvet Bridal Robe
 Luxe Satin Robe
 Classic Bridal Gown
 Bridal Satin Robe
 Night Gown Robe
 Bridal Lace Set
 Floral Satin Robe
 Soft Robe Set
 Cozy Bridal Robe
 Satin Robe Set
 Chic Lace Gown
 Elegant Silk Gown
 Luxe Gown Set
 Satin Wrap Robe
 Sleeveless Satin Set
 Winter Satin Gown
 Elegant Lace Set
 Luxury Kimono Robe
 Plush Satin Gown
 Silk Bathrobe Set
 Soft Bridal Gown
 Satin Kimono Set
 Luxe Robe Gown
 Bridal Gown Set
 Silk Satin Set
 Classic Satin Gown
 Cozy Spa Robe
 Satin Lace Set
 Luxe Robe Set
 Comfy Satin Gown
 Elegant Bridal Set
 Soft Kimono Robe
 Satin Gown Robe
 Luxury Satin Robe
 Bridal Lace Gown
 Luxe Velvet Robe
 Satin Bridal Set
"""

Long_Sleeved_Dress_l=r"""
 Elegant Long Sleeved Dress
 Casual Long Sleeved Dress
 Chic Long Sleeved Dress
 Classic Long Sleeved Dress
 Long Sleeve Maxi Dress
 Long Sleeve Bodycon Dress
 Soft Long Sleeved Dress
 Vintage Long Sleeved Dress
 Trendy Long Sleeved Dress
 Fitted Long Sleeved Dress
 Long Sleeved Party Dress
 Boho Long Sleeved Dress
 Button-up Long Sleeved Dress
 Comfortable Long Sleeved Dress
 Long Sleeve A-line Dress
 Sexy Long Sleeved Dress
 Formal Long Sleeved Dress
 Cozy Long Sleeved Dress
 Ruffled Long Sleeved Dress
 Flowy Long Sleeved Dress
 Simple Long Sleeved Dress
 Warm Long Sleeved Dress
 Office Long Sleeved Dress
 Maxi Long Sleeved Dress
 Turtleneck Long Sleeved Dress
 Loose Long Sleeved Dress
 Long Sleeved Casual Dress
 Floral Long Sleeved Dress
 Lace Long Sleeved Dress
 Velvet Long Sleeved Dress
 Sweater Long Sleeved Dress
 Classic Long Sleeve Dress
 Elegant Long Sleeve Dress
 Long Sleeve Midi Dress
 Long Sleeve Shift Dress
 Slim Fit Long Sleeved Dress
 Fitted Long Sleeve Dress
 Embellished Long Sleeved Dress
 Modern Long Sleeved Dress
 Simple Long Sleeve Dress
 Long Sleeve Holiday Dress
 Knit Long Sleeved Dress
 Long Sleeve T-shirt Dress
 Long Sleeved Cocktail Dress
 Long Sleeve Dress Style
 Sleeveless Long Sleeve Dress
 Layered Long Sleeved Dress
 Long Sleeved V-neck Dress
 High Neck Long Sleeved Dress
 Backless Long Sleeved Dress
 Bodycon Long Sleeved Dress
 Pleated Long Sleeved Dress
 Floral Print Long Dress
 A-line Long Sleeved Dress
 Loose Fit Long Sleeve Dress
 Tied Long Sleeved Dress
 Button-down Long Sleeve Dress
 Bohemian Long Sleeve Dress
 Long Sleeved Tunic Dress
 Long Sleeve Evening Dress
 Sexy Long Sleeve Gown
 Casual Long Sleeve Dress
 Soft Cotton Long Sleeved Dress
 Comfortable Long Sleeve Dress
 Cozy Long Sleeve Gown
 Luxe Long Sleeved Dress
 Stylish Long Sleeve Dress
 Long Sleeve Date Dress
 Long Sleeve Winter Dress
 Loose Long Sleeve Dress
 Straight Long Sleeve Dress
 Embroidered Long Sleeve Dress
 Stylish Long Sleeve Gown
 Polka Dot Long Dress
 Black Long Sleeve Dress
 Modern Long Sleeve Dress
 Ribbed Long Sleeved Dress
 Maxi Long Sleeve Dress
 Long Sleeve Mini Dress
 Warm Long Sleeve Dress
 Evening Long Sleeve Dress
 Knee-Length Long Sleeve Dress
 V-neck Long Sleeve Dress
 Printed Long Sleeve Dress
 High Waisted Long Dress
 Casual Long Sleeve Gown
 Fall Long Sleeved Dress
 Long Sleeve Satin Dress
 Stylish Long Sleeved Gown
 Wool Long Sleeved Dress
 Long Sleeve Knit Dress
 Cozy Long Sleeve Tunic
 Bodycon Long Sleeve Dress
 Slim Long Sleeve Dress
 Winter Long Sleeved Dress
 Trendy Long Sleeve Dress
 Long Sleeve Pencil Dress
 Warm Long Sleeve Gown
 Long Sleeve Pleated Dress
 Flared Long Sleeved Dress
"""

Pajama_Sets_l=r"""
 Women's pajama sets
 Men's pajama sets
 Kids' pajama sets
 Baby pajama sets
 Couple pajama sets
 Family matching pajama sets
 Plus size pajama sets
 Petite pajama sets
 Maternity pajama sets
 Unisex pajama sets
 Cotton pajama sets
 Silk pajama sets
 Satin pajama sets
 Flannel pajama sets
 Fleece pajama sets
 Linen pajama sets
 Bamboo pajama sets
 Velvet pajama sets
 Polyester pajama sets
 Knitted pajama sets
 Summer pajama sets
 Winter pajama sets
 Spring pajama sets
 Fall pajama sets
 Lightweight pajama sets
 Breathable pajama sets
 Warm pajama sets
 Cooling pajama sets
 Cozy pajama sets
 Thermal pajama sets
 Cute pajama sets
 Sexy pajama sets
 Elegant pajama sets
 Minimalist pajama sets
 Classic pajama sets
 Boho pajama sets
 Vintage pajama sets
 Chic pajama sets
 Cartoon pajama sets
 Floral pajama sets
 Long sleeve pajama sets
 Short sleeve pajama sets
 Sleeveless pajama sets
 Button-up pajama sets
 Two-piece pajama sets
 Three-piece pajama sets
 Hoodie pajama sets
 Jogger pajama sets
 Camisole pajama sets
 Shorts pajama sets
 Loungewear pajama sets
 Bridal pajama sets
 Travel pajama sets
 Nursing pajama sets
 Postpartum pajama sets
 Sleepwear pajama sets
 Party pajama sets
 Work-from-home pajama sets
 Spa pajama sets
 Movie night pajama sets
 Victoria’s Secret pajama sets
 Calvin Klein pajama sets
 H&M pajama sets
 Zara pajama sets
 Forever 21 pajama sets
 Shein pajama sets
 Target pajama sets
 Nordstrom pajama sets
 Macy’s pajama sets
 Amazon pajama sets
 Affordable pajama sets
 Cheap pajama sets
 Luxury pajama sets
 Designer pajama sets
 Budget-friendly pajama sets
 Expensive pajama sets
 High-end pajama sets
 Discounted pajama sets
 Best-value pajama sets
 Pajama sets under $50
 Best pajama sets for hot sleepers
 Best pajama sets for cold weather
 Best pajama sets for sensitive skin
 Best pajama sets for pregnancy
 Best pajama sets for teens
 Best pajama sets for elderly women
 Best pajama sets for lounging
 Best pajama sets for honeymoon
 Best pajama sets for relaxing weekends
 Best pajama sets for girls' night
 Matching couple pajama sets
 Personalized pajama sets
 Custom pajama sets with names
 Funny graphic pajama sets
 Pajama sets with pockets
 Softest pajama sets
 Breathable cotton pajama sets
 Cozy winter pajama sets
 Trendy pajama sets for women
 Best-selling pajama sets 2024
"""

Plus_Size_Dress_l=r"""
 Elegant Plus Size
 Casual Plus Dress
 Plus Size Gown
 Chic Plus Size
 Plus Size Midi
 Floral Plus Dress
 Plus Size Party
 Plus Size Maxi
 Sexy Plus Dress
 Stylish Plus Dress
 Plus Size Outfit
 Formal Plus Dress
 Plus Size Style
 Plus Size Fit
 Plus Size Chic
 Trendy Plus Size
 Plus Size Fashion
 Comfortable Plus Dress
 Plus Size Casual
 Elegant Plus Gown
 Plus Size Cocktail
 Sleeveless Plus Dress
 Plus Size Evening
 Bold Plus Size
 Plus Size Top
 Plus Size Wrap
 Plus Size T-shirt
 Plus Size V-neck
 Plus Size Shift
 Plus Size Jumpsuit
 Boho Plus Dress
 Plus Size Romper
 Plus Size Blouse
 Plus Size Dressy
 Cozy Plus Dress
 Casual Plus Gown
 Plus Size Embellished
 Plus Size Lace
 Bodycon Plus Size
 Plus Size Tunic
 Plus Size Ruffle
 Bold Plus Gown
 Plus Size Colorblock
 Trendy Plus Gown
 Plus Size Skirt
 Formal Plus Gown
 Plus Size Pleated
 Plus Size Sleeveless
 Plus Size High-low
 Plus Size Floral
 Plus Size A-line
 Plus Size Long
 Plus Size Fitted
 Plus Size Boho
 Plus Size Swing
 Plus Size Ruffles
 Summer Plus Dress
 Plus Size Spaghetti
 Plus Size Day
 Plus Size Long-sleeve
 Plus Size Skater
 Plus Size Sleeves
 Simple Plus Dress
 Plus Size Mesh
 Plus Size Trendy
 Comfortable Plus Gown
 Plus Size Elegant
 Plus Size Satin
 Plus Size Slit
 Plus Size Embroidered
 Plus Size Cold-shoulder
 Stylish Plus Gown
 Plus Size Off-shoulder
 Plus Size Glitter
 Plus Size Formal
 Plus Size Knee-length
 Plus Size Frock
 Plus Size Dress
 Plus Size Sleeved
 Plus Size Sexy
 Plus Size Summer
 Plus Size Luxe
 Plus Size Flowing
 Plus Size Belted
 Plus Size Ruched
 Plus Size Buttoned
 Plus Size Cowl-neck
 Plus Size Fit-and-flare
 Plus Size Polka-dots
 Plus Size Blouson
 Plus Size Wide-leg
 Plus Size Bodycon
 Plus Size Stylish
 Trendy Plus Dress
 Chic Plus Dress
 Stylish Plus Size
 Comfy Plus Dress
 Flattering Plus Dress
 Elegant Plus Size Dress
 Trendy Plus Size Gown
"""

Hoodies_Sweatshirts_l=r"""
 Cozy Hoodies & Sweatshirts
 Stylish Hoodies Collection
 Warm Sweatshirts for Women
 Casual Hoodie Style
 Comfy Sweatshirts for Women
 Trendy Hoodie Sweatshirt
 Hoodies & Sweatshirts Fashion
 Loose Fit Hoodie Sweatshirt
 Soft Hoodies for Women
 Classic Hoodie Sweatshirt
 Oversized Hoodies for Women
 Casual Women’s Hoodies
 Graphic Sweatshirts Collection
 Chic Hoodie Sweatshirt
 Lightweight Hoodie Sweatshirt
 Cozy Sweatshirts for Fall
 Printed Hoodies for Women
 Fleece Hoodies & Sweatshirts
 Women’s Zip-up Hoodies
 Casual Hoodie Sweatshirt Look
 Comfortable Women’s Hoodies
 Pullover Hoodie Sweatshirt
 Warm Sweatshirt Designs
 Hoodie Sweatshirt Trend
 Hooded Sweatshirt for Women
 Elegant Hoodies & Sweatshirts
 Cotton Hoodie Sweatshirt
 Relaxed Fit Sweatshirts
 Everyday Hoodie Sweatshirt
 Casual Sweatshirts for Women
 Warm Hoodie Sweatshirt
 Hoodies for Winter Wear
 Soft Sweatshirts for Women
 Cozy Hoodie Pullover
 Basic Hoodie Sweatshirt
 Women’s Hoodie with Pockets
 High-neck Sweatshirt Hoodie
 Trendy Women’s Hoodies
 Sporty Sweatshirts for Women
 Hoodies & Sweatshirts Combo
 Stylish Pullover Hoodie
 Simple Hoodies for Women
 Graphic Hoodie Sweatshirt
 Warm Fleece Sweatshirts
 Modern Hoodie Sweatshirt
 Cozy Zip Hoodie
 Casual Pullover Hoodies
 Hoodie Sweatshirt for Fall
 Comfy Sweatshirts for Fall
 Hoodie Sweatshirt Fashion
 Women’s Hoodie with Logo
 Zip-up Sweatshirt Look
 Hoodies for Streetwear
 Relaxed Sweatshirt Look
 Women’s Oversized Hoodie
 All-season Hoodie Sweatshirt
 Hoodie Sweatshirt Chic
 Printed Hooded Sweatshirts
 Cozy Winter Sweatshirt
 Soft Hooded Sweatshirt
 Sporty Hoodie Sweatshirt
 Comfortable Hoodie Sweatshirt
 Hoodie Sweatshirt Set
 Long Sleeve Hoodie
 Casual Hoodie Sweatshirt Wear
 Fleece Zip-up Hoodie
 Trendy Sweatshirt Hoodie
 Basic Hoodie Sweatshirt Look
 Hoodie Sweatshirt with Logo
 Relaxed Hoodie Sweatshirt Fit
 Colorblock Hoodie Sweatshirt
 Classic Zip Hoodie
 Warm Hoodie Sweatshirt Style
 Stylish Sweatshirt Look
 Plush Hoodie Sweatshirt
 Fashion Hoodie Sweatshirt
 Comfy Pullover Sweatshirt
 Cozy Sweatshirt Design
 Lightweight Zip Hoodie
 Casual Graphic Hoodies
 Street Style Hoodies
 Women’s Hoodie Pullover
 Soft Cotton Hoodie
 Zip-up Hoodie for Women
 Relaxed Fit Hoodie
 Hoodie with Drawstrings
 Long Hoodie Sweatshirt
 Cozy Women’s Hoodie
 Fashionable Sweatshirts for Women
 Pullover Hoodie Sweatshirt Trend
 Printed Sweatshirt Hoodie
 Women’s Hoodie Sweater
 Comfort Hoodie Sweatshirt
 Soft Sweatshirts with Logo
 Sweatshirt Hoodie Collection
 Classic Women’s Sweatshirt
 Bold Hoodie Sweatshirt
 Lightweight Hooded Sweatshirt
 Women’s Pullover Hoodie
 Winter Hoodie Sweatshirt
"""

Bodycon_Dress_l=r"""
 Sexy Bodycon Dress
 Chic Bodycon Gown
 Sleeveless Bodycon Dress
 Elegant Bodycon Dress
 Casual Bodycon Dress
 Classic Bodycon Dress
 Bodycon Midi Dress
 Tight Fit Dress
 Bold Bodycon Dress
 High Neck Bodycon
 Off-shoulder Bodycon Dress
 Bodycon Evening Dress
 Bodycon Cocktail Dress
 Flirty Bodycon Dress
 Short Bodycon Dress
 Velvet Bodycon Dress
 Satin Bodycon Dress
 Long Sleeve Bodycon
 Strappy Bodycon Dress
 Bodycon Dress Set
 Lace Bodycon Dress
 Ruffle Bodycon Dress
 Bodycon Dress Outfit
 Sexy Mini Bodycon
 Colorblock Bodycon Dress
 Spaghetti Strap Bodycon
 Fitted Bodycon Dress
 Bodycon Pencil Dress
 Bodycon Wrap Dress
 Night Out Dress
 Formal Bodycon Dress
 Stretch Bodycon Dress
 Bodycon Dress Chic
 Hot Pink Bodycon
 Black Bodycon Dress
 Bodycon Dress Style
 Lace Detail Bodycon
 Off-shoulder Bodycon
 Bodycon Dress Night
 Summer Bodycon Dress
 Bodycon Fashion Dress
 Elegant Bodycon Gown
 Slim Fit Dress
 Party Bodycon Dress
 Stylish Bodycon Dress
 Ruched Bodycon Dress
 Bodycon Dress Trend
 Classic Black Bodycon
 Stylish Bodycon Gown
 White Bodycon Dress
 Sexy Slim Dress
 Bodycon Evening Gown
 Trendy Bodycon Dress
 V-neck Bodycon Dress
 Stylish Mini Bodycon
 Bodycon Dress Look
 Bodycon Dress Summer
 Fitted Mini Bodycon
 Bodycon Party Dress
 Sparkling Bodycon Dress
 Bodycon Dress Fit
 Elegant Bodycon Fit
 Sexy Red Bodycon
 Bodycon Dress Curve
 Fashion Bodycon Dress
 Bodycon Dress Sleek
 Hot Bodycon Dress
 Simple Bodycon Dress
 Bodycon Wrap Gown
 Lace Back Bodycon
 Bodycon Dress Casual
 Elegant Slim Bodycon
 Bold Bodycon Style
 Sexy Midi Bodycon
 Bodycon Dress Party
 Sleek Bodycon Dress
 Bodycon Gown Chic
 Simple Bodycon Gown
 Plunging Bodycon Dress
 Bodycon Dress Classic
 Sheer Bodycon Dress
 Sleeveless Bodycon Gown
 Stylish Bodycon Midi
 Off-shoulder Dress Set
 Trendy Bodycon Gown
 Mesh Bodycon Dress
 Luxe Bodycon Dress
 Bodycon Dress Glam
 Figure-hugging Bodycon Dress
 Glam Bodycon Dress
 Sexy Bodycon Gown
 Bold Bodycon Look
 Curvy Bodycon Dress
 Bodycon Dress Fashion
 Form-fitting Bodycon Dress
 Mesh Bodycon Gown
 Sweetheart Bodycon Dress
 All-black Bodycon Dress
 Lace Trim Bodycon
 Chic Bodycon Fit
"""

Lace_Dress_l=r"""
 Elegant Lace Dress
 Lace Evening Dress
 Sexy Lace Dress
 Floral Lace Dress
 Lace Cocktail Dress
 Lace Wedding Dress
 Classic Lace Dress
 Lace Bodycon Dress
 Lace Party Dress
 Vintage Lace Dress
 Lace Midi Dress
 Lace A-line Dress
 Chic Lace Dress
 Romantic Lace Dress
 White Lace Dress
 Black Lace Dress
 Lace Dress Set
 Long Sleeve Lace Dress
 Lace Bridesmaid Dress
 Off-shoulder Lace Dress
 Ruffled Lace Dress
 Lace Maxi Dress
 Lace Shift Dress
 Lace Detail Dress
 Lace Cocktail Gown
 Simple Lace Dress
 Lace Dress Chic
 Lace Dress Trend
 Sleeveless Lace Dress
 Boho Lace Dress
 Lace Dress Vibe
 Lace Dress Fashion
 Tiered Lace Dress
 Pink Lace Dress
 Lace Dress Glam
 Elegant Lace Gown
 Lace Dress Design
 Lace Dress Casual
 Lace Dress Formal
 Lace Dress Look
 Lace Dress Bohemian
 Sexy Lace Gown
 Lace Dress Fit
 Blue Lace Dress
 Lace Dress Style
 Lace Dress Shine
 Casual Lace Dress
 Modern Lace Dress
 Lace Skater Dress
 Lace Fit-and-Flare
 Lace Wedding Gown
 Lace Dress Party
 Lace Dress Sparkle
 Lace Dress Glamour
 Sheer Lace Dress
 Lace Dress Accent
 Lace Detail Gown
 Lace Dress Sleek
 Lace Dress with Belt
 Lace Gown Glam
 Lace Dress Sparkly
 Simple Lace Gown
 Lace Dress Twirl
 Lace Dress Day
 Lace Dress Lookbook
 Lace Dress Layers
 Lace High Neck Dress
 Lace Dress Trendy
 Off-the-shoulder Lace
 Lace Dress Flare
 Lace Dress Elegance
 Lace Gown Style
 Soft Lace Dress
 Light Lace Dress
 Lace Party Gown
 Ruffled Lace Gown
 Lace Dress Appeal
 Full Lace Dress
 Lace Evening Gown
 Lace Dress for Women
 Elegant Lace Design
 Lace Dress Classic
 Bohemian Lace Dress
 Lace Dress Dreamy
 Lace Dress Summer
 Lace Mini Dress
 Lace Dress Glamorous
 Flowy Lace Dress
 Lace Dress Lace
 Lace Bridesmaid Gown
 Lace Dress Perfect
 Lace Overlay Dress
 Lace Dress Glow
 Vintage Lace Gown
 Satin Lace Dress
 Lace Dress for Weddings
 Tiered Lace Gown
 Lace Dress Deep V
 Layered Lace Dress
 Lace Dress Modern
"""

Sweater_Dresses_l=r"""
 Cozy Sweater Dress
 Chunky Knit Sweater Dress
 Casual Sweater Dress
 Elegant Sweater Dress
 Oversized Sweater Dress
 Winter Sweater Dress
 Wool Sweater Dress
 V-neck Sweater Dress
 Long Sleeve Sweater Dress
 Knitted Sweater Dress
 Fitted Sweater Dress
 Sweater Dress Chic
 Stylish Sweater Dress
 Cozy Knit Sweater Dress
 Soft Sweater Dress
 Sweater Dress Outfit
 Casual Knit Sweater
 Knit Sweater Dress
 Sweater Dress Fashion
 Sweater Dress Casual
 Slim Fit Sweater Dress
 Sweater Dress with Belt
 Casual Winter Sweater
 Layered Sweater Dress
 Oversized Knit Dress
 Soft Knit Sweater
 Bodycon Sweater Dress
 Sweater Dress Trendy
 Long Knit Sweater Dress
 High Neck Sweater Dress
 Woolen Sweater Dress
 Cozy Dress Sweater
 Sweater Dress Fit
 Chunky Knit Dress
 Winter Knit Dress
 Warm Sweater Dress
 Fashion Sweater Dress
 Sleeveless Sweater Dress
 Knit Dress Chic
 Midi Sweater Dress
 Loose Sweater Dress
 Stylish Knit Dress
 Ribbed Sweater Dress
 Cozy Winter Dress
 Sweater Dress Look
 Turtleneck Sweater Dress
 Knit Sweater Gown
 Sweater Dress Vibe
 Classic Sweater Dress
 Warm Knit Sweater
 Comfortable Sweater Dress
 Chunky Sweater Dress
 Fitted Knit Sweater
 Elegant Knit Sweater
 Holiday Sweater Dress
 Sweater Dress Elegant
 Long Sleeve Knit Dress
 Knit Winter Sweater
 Knit Bodycon Sweater
 Simple Sweater Dress
 Cozy Knit Dress
 Sweater Dress Style
 Lightweight Sweater Dress
 Comfy Sweater Dress
 Stretch Sweater Dress
 Classic Knit Sweater
 Knit Sleeve Dress
 Ribbed Knit Sweater
 Lace Sweater Dress
 Sweater Dress Lookbook
 Chic Knit Dress
 Slouchy Sweater Dress
 Fitted Sweater Gown
 Trendy Sweater Dress
 Flared Sweater Dress
 Comfy Knit Dress
 Sweater Dress with Pockets
 Simple Knit Sweater
 Cozy Bodycon Sweater
 Fall Sweater Dress
 Sweater Dress Details
 Sweater Dress Twist
 Sleek Sweater Dress
 Warm Wool Sweater
 High Neck Knit Dress
 Cozy Sweater Gown
 Trendy Knit Sweater
 Sweater Dress Combo
 Long Sleeve Sweater
 Turtleneck Knit Dress
 Color Block Sweater
 Sweater Dress Cozy
 Loose Knit Sweater
 Casual Sweater Gown
 Knitted Sweater Gown
 Sweater Dress Glam
 Soft Wool Sweater
 Fall Knit Sweater
 Cozy Knit Gown
 Chunky Knit Sweater
"""

Sequin_Dress_l=r"""
 Glamorous Sequin Dress
 Elegant Sequin Dress
 Sexy Sequin Dress
 Chic Sequin Dress
 Party Sequin Dress
 Sparkling Sequin Dress
 Sequin Evening Dress
 Formal Sequin Dress
 Sequin Cocktail Dress
 Sequin Party Dress
 Sexy Sequin Gown
 Sequin Mini Dress
 Sequin Maxi Dress
 Sequin Bodycon Dress
 Sequin A-line Dress
 Sleek Sequin Dress
 Colorful Sequin Dress
 Gold Sequin Dress
 Silver Sequin Dress
 Black Sequin Dress
 Pink Sequin Dress
 Sequin Dress Chic
 Sequin Dress Style
 Elegant Sequin Gown
 Sparkly Sequin Dress
 Sequin Dress Trend
 Blue Sequin Dress
 Sequin Dress Glam
 Sequin Dress Look
 Glitter Sequin Dress
 Sequin Wrap Dress
 Sequin Shift Dress
 Sequin Fit Dress
 Sequin Dress Outfit
 Sequin Dress Sexy
 Long Sleeve Sequin
 Sequin Dress Casual
 Ruffled Sequin Dress
 Sequin Dress Fashion
 Sequin Dress Appeal
 V-neck Sequin Dress
 Strapless Sequin Dress
 Sequin Backless Dress
 Sequin Dress Night
 Sequin Slip Dress
 Sequin Detail Dress
 Party Wear Sequin
 Sequin Dress Sleeveless
 Off-shoulder Sequin Dress
 High Neck Sequin
 Sequin Dress Trendy
 Formal Sequin Gown
 Sexy Sequined Dress
 Shimmer Sequin Dress
 Metallic Sequin Dress
 Floor-length Sequin Dress
 Vintage Sequin Dress
 Sequin Dress Glamour
 Sequin Dress Sparkle
 Sequin Gown Chic
 Sparkly Mini Sequin
 Sequin Dress Party
 Sequin Cocktail Gown
 Sequin Dress Dressy
 Beautiful Sequin Dress
 Hot Pink Sequin
 Silver Glitter Sequin
 Sequin Dress Allure
 Sequin Gown Party
 Sleeveless Sequin Dress
 Short Sequin Dress
 Sequin Shift Gown
 Shiny Sequin Dress
 Glam Sequin Dress
 Stylish Sequin Dress
 Sequin Dress Midi
 Modern Sequin Dress
 Flirty Sequin Dress
 Sequin Dress Shine
 Flared Sequin Dress
 Plus Size Sequin
 All-Over Sequin Dress
 Black Sequin Gown
 Sequin Dress Long
 Sequin Lace Dress
 Ruched Sequin Dress
 High Waist Sequin
 Bodycon Sequin Dress
 Sequin Dress Fit
 Off-shoulder Sequin
 Satin Sequin Dress
 Elegant Glitter Sequin
 Sequin Dress Vibe
 Pink Sequin Gown
 Sequin Dress Twist
 Backless Sequin Dress
 Lush Sequin Dress
 Bright Sequin Dress
 Modern Sequin Gown
 Classy Sequin Dress
"""

Tulle_Dress_l=r"""
 Elegant Tulle Dress
 Fluffy Tulle Dress
 Chic Tulle Dress
 Tulle Evening Dress
 Party Tulle Dress
 Tulle Ball Gown
 Romantic Tulle Dress
 Tulle Maxi Dress
 Tulle Cocktail Dress
 Tulle Lace Dress
 Soft Tulle Dress
 Tulle Wedding Dress
 Tulle A-line Dress
 Tulle Bodycon Dress
 Casual Tulle Dress
 Tulle Dress Chic
 Boho Tulle Dress
 Tulle Skirt Dress
 Tulle Dress Trend
 Stylish Tulle Dress
 Pink Tulle Dress
 Black Tulle Dress
 White Tulle Dress
 Tulle Dress Glam
 Vintage Tulle Dress
 Tulle Dress Sparkle
 Elegant Tulle Gown
 Tulle Dress Set
 Tulle Dress Outfit
 Tulle Dress Style
 Sexy Tulle Dress
 Off-shoulder Tulle Dress
 Ruffled Tulle Dress
 Lace Tulle Dress
 Tulle Dress Fashion
 Floor-length Tulle Dress
 Tulle Dress Sparkling
 Tulle Dress Look
 Tiered Tulle Dress
 Long Sleeve Tulle
 Tulle Dress Dream
 Sweet Tulle Dress
 Sequin Tulle Dress
 Tulle Dress Formal
 Tulle Dress Design
 Tulle Dress Classic
 Romantic Tulle Gown
 Tulle Dress Ruffles
 Tulle Party Dress
 Tulle Dress Vibe
 Tulle Dress Fit
 Tulle Dress Trendy
 Tulle Dress Glow
 Tulle Dress Twirl
 Tulle Dress Occasion
 Tulle Wedding Gown
 Classic Tulle Dress
 Tulle Midi Dress
 Stylish Tulle Gown
 Tulle Dress Puff
 Pleated Tulle Dress
 Tulle Dress Flare
 Soft Tulle Gown
 Tulle Dress Perfect
 Formal Tulle Dress
 Tulle Dress Glamour
 Bohemian Tulle Dress
 Tulle Dress Party
 Casual Tulle Gown
 Tulle Bridesmaid Dress
 Short Tulle Dress
 A-line Tulle Dress
 Tulle Dress Fluffy
 Tulle Dress Sleek
 Full Tulle Dress
 Tulle Dress Sparkly
 Tulle Dress Layers
 Tulle Evening Gown
 Tulle Dress Charm
 Soft Layered Tulle
 Tulle Dress Silhouette
 Boho Chic Tulle
 Tulle Dress Flow
 Tulle Dress Blush
 Tulle Dress Simple
 Tulle Dress Color
 White Lace Tulle
 Blue Tulle Dress
 Tulle Dress Dazzle
 Ruffled Tulle Gown
 A-line Tulle Gown
 Pretty Tulle Dress
 Glitter Tulle Dress
 Tulle Dress Modern
 Tulle Party Gown
 Tulle Dress Shine
 Tulle Lace Gown
 Pink Tulle Gown
 Tulle Dress Soft
 Sparkling Tulle Dress
"""

Maxi_Dresses_l=r"""
 Hot new arrivals in maxi dresses
 Women's maxi dresses
 Summer maxi dresses
 Casual maxi dresses
 Party maxi dresses
 Elegant maxi dresses
 Sexy maxi dresses
 Long sleeve maxi dresses
 Sleeveless maxi dresses
 Strapless maxi dresses
 Off-shoulder maxi dresses
 Cotton maxi dresses
 Satin maxi dresses
 Silk maxi dresses
 Lace maxi dresses
 Denim maxi dresses
 Velvet maxi dresses
 Chiffon maxi dresses
 Knitted maxi dresses
 Sequin maxi dresses
 Leather maxi dresses
 Wedding guest maxi dresses
 Date night maxi dresses
 Cocktail maxi dresses
 Beach maxi dresses
 Vacation maxi dresses
 Formal maxi dresses
 Office maxi dresses
 Graduation maxi dresses
 Festival maxi dresses
 Holiday maxi dresses
 Vintage maxi dresses
 Boho maxi dresses
 Chic maxi dresses
 Y2K maxi dresses
 Edgy maxi dresses
 Minimalist maxi dresses
 Glamorous maxi dresses
 Street style maxi dresses
 Preppy maxi dresses
 Goth maxi dresses
 Zara maxi dresses
 H&M maxi dresses
 Forever 21 maxi dresses
 PrettyLittleThing maxi dresses
 Shein maxi dresses
 Revolve maxi dresses
 ASOS maxi dresses
 Fashion Nova maxi dresses
 Boohoo maxi dresses
 Urban Outfitters maxi dresses
 Stretchy maxi dresses
 Flowy maxi dresses
 Bodycon maxi dresses
 Wrap maxi dresses
 Smocked maxi dresses
 Ruffled maxi dresses
 Tiered maxi dresses
 A-line maxi dresses
 Corset maxi dresses
 Halter maxi dresses
 Summer party maxi dresses
 Winter maxi dresses
 Spring maxi dresses
 Fall maxi dresses
 Birthday maxi dresses
 Anniversary maxi dresses
 Clubbing maxi dresses
 Prom maxi dresses
 Red carpet maxi dresses
 New Year's Eve maxi dresses
 Affordable maxi dresses
 Cheap maxi dresses
 Luxury maxi dresses
 Designer maxi dresses
 Budget-friendly maxi dresses
 Expensive maxi dresses
 High-end maxi dresses
 Discounted maxi dresses
 Best value maxi dresses
 Trendy maxi dresses under $50
 Best maxi dresses for petites
 Best maxi dresses for curvy figures
 Best maxi dresses for tall women
 Best maxi dresses for plus size
 Best maxi dresses for hourglass body shape
 Best maxi dresses for date night
 Best maxi dresses for casual wear
 Best maxi dresses for formal events
 Best maxi dresses for summer vacation
 Best maxi dresses for elegant looks
 Women's trendy maxi dresses sale
 Sexy little black maxi dresses
 Cute floral print maxi dresses
 Comfortable maxi dresses for everyday wear
 Fashion-forward maxi dresses
 Lightweight maxi dresses for hot weather
 Versatile maxi dresses for all occasions
 Flattering maxi dresses for all body types
 Must-have maxi dresses for this season
"""

Sweater_l=r"""
 Women's sweaters
 Men's sweaters
 Kids' sweaters
 Oversized sweaters
 Cropped sweaters
 Turtleneck sweaters
 V-neck sweaters
 Crewneck sweaters
 Cardigan sweaters
 Zip-up sweaters
 Wool sweaters
 Cotton sweaters
 Cashmere sweaters
 Knitted sweaters
 Fleece sweaters
 Chunky knit sweaters
 Acrylic sweaters
 Silk-blend sweaters
 Mohair sweaters
 Alpaca wool sweaters
 Winter sweaters
 Fall sweaters
 Spring sweaters
 Lightweight sweaters
 Warm sweaters
 Thermal sweaters
 Layering sweaters
 Outdoor sweaters
 Travel-friendly sweaters
 Office sweaters
 Casual sweaters
 Elegant sweaters
 Minimalist sweaters
 Vintage sweaters
 Streetwear sweaters
 Classic sweaters
 Fashionable sweaters
 Sporty sweaters
 Boho-style sweaters
 Edgy sweaters
 Nike sweaters
 Adidas sweaters
 North Face sweaters
 Columbia sweaters
 Patagonia sweaters
 Canada Goose sweaters
 Levi's sweaters
 H&M sweaters
 Zara sweaters
 Gucci sweaters
 Breathable sweaters
 Moisture-wicking sweaters
 Wrinkle-resistant sweaters
 Stretchable sweaters
 UV protection sweaters
 Water-resistant sweaters
 Thermal insulation sweaters
 Anti-pilling sweaters
 Soft-touch sweaters
 Eco-friendly sweaters
 Work sweaters
 Date night sweaters
 Party sweaters
 College sweaters
 Weekend sweaters
 Formal sweaters
 Christmas sweaters
 Thanksgiving sweaters
 Holiday sweaters
 Travel sweaters
 Affordable sweaters
 Cheap sweaters
 Luxury sweaters
 Premium sweaters
 Budget-friendly sweaters
 Designer sweaters
 Expensive sweaters
 High-end sweaters
 Best value sweaters
 Discounted sweaters
 Best sweaters for winter
 Best sweaters for layering
 Best sweaters for travel
 Best sweaters for work
 Best sweaters for fall
 Best sweaters for cold weather
 Best sweaters for hiking
 Best sweaters for cozy nights
 Best sweaters for casual wear
 Best sweaters for formal occasions
 Women's fashion sweaters sale
 Men's wool sweaters discount
 Warmest sweaters for extreme cold
 Softest cashmere sweaters
 Trendy oversized sweaters
 Best everyday sweaters
 Comfortable sweaters for all seasons
 Lightweight sweaters for spring
 Cozy knit sweaters for winter
 Must-have sweaters for this season
"""

Tank_Dress_l=r"""
 Casual Tank Dress
 Sleeveless Tank Dress
 Simple Tank Dress
 Summer Tank Dress
 Elegant Tank Dress
 Chic Tank Dress
 Tank Dress Style
 Loose Fit Tank Dress
 Stylish Tank Dress
 Bodycon Tank Dress
 Mini Tank Dress
 Flowy Tank Dress
 Ruffle Tank Dress
 High-Waisted Tank Dress
 Comfortable Tank Dress
 Tank Dress Trend
 Casual Tank Dress Look
 Tank Dress Fashion
 Lightweight Tank Dress
 Tank Dress Outfit
 Summer Ready Tank
 Classic Tank Dress
 Simple Sleeveless Dress
 Relaxed Tank Dress
 Spaghetti Strap Tank Dress
 Soft Tank Dress
 Printed Tank Dress
 Tank Dress Casual
 Tank Dress Party
 Black Tank Dress
 Boho Tank Dress
 Tank Dress Glam
 Loose Tank Dress
 Chic Sleeveless Dress
 Tank Dress Vibe
 Pleated Tank Dress
 Tank Dress Fun
 A-line Tank Dress
 Basic Tank Dress
 Floral Tank Dress
 Off-shoulder Tank Dress
 Vintage Tank Dress
 Comfortable Sleeveless Dress
 Sexy Tank Dress
 Tank Dress Style Look
 Modern Tank Dress
 Trendy Tank Dress
 Casual Chic Tank Dress
 Soft Fabric Tank Dress
 Sleeveless Bodycon Tank
 Minimalist Tank Dress
 Tank Dress Twist
 Solid Tank Dress
 Stylish Tank Gown
 Fitted Tank Dress
 Tank Dress Layered
 Tank Dress Shine
 Elegant Sleeveless Dress
 Bold Tank Dress
 Tied Tank Dress
 Pleated Sleeveless Dress
 Fit-and-Flare Tank Dress
 Tank Dress Silhouette
 Backless Tank Dress
 Summer Tank Dress Vibe
 Soft Tank Dress Trend
 Light Tank Dress
 Sexy Sleeveless Tank
 Trendy Sleeveless Dress
 White Tank Dress
 Stretch Tank Dress
 A-line Sleeveless Dress
 Tank Dress Glamour
 Sleeveless Tank Gown
 T-shirt Tank Dress
 Tank Dress Comfort
 Spaghetti Strap Dress
 Tank Dress Combination
 Relaxed Fit Tank Dress
 Easygoing Tank Dress
 Everyday Tank Dress
 Tank Dress with Pockets
 Vintage Sleeveless Tank
 Fashion Tank Dress
 Soft Cotton Tank Dress
 Tank Dress Layer
 Chic Casual Tank Dress
 Basic Sleeveless Tank
 Tank Dress for Women
 Trendy Tank Dress Look
 Sleeveless Casual Dress
 Ruffled Tank Dress
 Tank Dress Casual Chic
 Comfortable Tank Gown
 Bohemian Tank Dress
 Tank Dress Relaxed Fit
 Tank Dress for Summer
 Feminine Tank Dress
 Ripped Tank Dress
 Cool Tank Dress
"""


# for websiteId in range(788,793):
# add_houzhui(websiteId=793, classificationId='2251937252638720', newValue='')

# 1053-1112
# 2601
for websiteId in range(300,343+1):
    try:
        add_houzhui(websiteId=websiteId, classificationId='2252762255458304', newValue=Lace_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762272235520', newValue=Pencil_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252349754048512', newValue=Sweater_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762087686144', newValue=Mini_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762238681088', newValue=Sweater_Dresses_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762104463360', newValue=Midi_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252761987022848', newValue=Mini_Dresses_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252761970245632', newValue=Unclassified_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762221903872', newValue=Denim_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252761919913984', newValue=Party_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762188349440', newValue=Tulle_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252761953468416', newValue=Wedding_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762154795008', newValue=Tank_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762054131712', newValue=Floral_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252899509862400', newValue=Swimsuit_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762138017792', newValue=Suspender_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762171572224', newValue=Sequin_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762003800064', newValue=Midi_Dresses_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762205126656', newValue=Shirt_Dress_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252761936691200', newValue=Unclassified_Dresses_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762020577280', newValue=Maxi_Dresses_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2252762121240576', newValue=Maxi_Skirt_l.rstrip())
        add_houzhui(websiteId=websiteId, classificationId='2251937252638720', newValue=Hoodies_Sweatshirts_l.rstrip())

        # add_houzhui(websiteId=websiteId, classificationId='2252074859364352', newValue=Blazers_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762272235520', newValue=Pencil_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762221903872', newValue=Denim_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762087686144', newValue=Mini_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761987022848', newValue=Mini_Dresses_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761970245632', newValue=Unclassified_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761919913984', newValue=Party_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761953468416', newValue=Wedding_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762054131712', newValue=Floral_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762205126656', newValue=Shirt_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252074876141568', newValue=Pullovers_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762138017792', newValue=Suspender_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762121240576', newValue=Maxi_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762104463360', newValue=Midi_Skirt_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252074725146624', newValue=Womens_Jackets_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762003800064', newValue=Midi_Dresses_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761936691200', newValue=Unclassified_Dresses_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='3377837193035776', newValue=Robe_Gown_Sets_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762070908928', newValue=Long_Sleeved_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='3377837176258560', newValue=Pajama_Sets_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762037354496', newValue=Plus_Size_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2251937252638720', newValue=Hoodies_Sweatshirts_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252761903136768', newValue=Bodycon_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762255458304', newValue=Lace_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762238681088', newValue=Sweater_Dresses_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762171572224', newValue=Sequin_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762188349440', newValue=Tulle_Dress_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762020577280', newValue=Maxi_Dresses_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252349754048512', newValue=Sweater_l.rstrip())
        # add_houzhui(websiteId=websiteId, classificationId='2252762154795008', newValue=Tank_Dress_l.rstrip())
    except:
        print(websiteId,"有问题!")

func_l = r"""
add_houzhui(websiteId=websiteId, classificationId='2252075329126400', newValue=Outerwears_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075262017536', newValue=Overalls_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074993582080', newValue=Overcoat_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074892918784', newValue=Vest_Coats_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075228463104', newValue=Bomber_Jacket_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487075573760', newValue=Blouses_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624497737728', newValue=Shorts_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487276888064', newValue=Bottoming_Shirt_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487293665280', newValue=Sun Protection_Clothing_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624665509888', newValue=Overalls_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252349754048512', newValue=Woolen_Sweater_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624548069376', newValue=Bottom_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252899509862400', newValue=Swimsuit_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='3377974615220224', newValue=Bras_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252762205126656', newValue=Floral_Skirt_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075043913728', newValue=Raincoat_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074775478272', newValue=Down_Coats_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075278794752', newValue=Ski_Suit_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075027136512', newValue=Cape_Coats_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487193001984', newValue=Top_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624464183296', newValue=Pants_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074758701056', newValue=Trench_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252075362680832', newValue=Shawl_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074708369408', newValue=Waistcoats_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487075565568', newValue=Short_Sleeve_Shirts_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252761987022848', newValue=Mini_Dresses_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252762020577280', newValue=Maxi_Dressesl.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624598401024', newValue=Jeans_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624531304448', newValue=Legging_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252762003800064', newValue=Midi_Dresses_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252762070908928', newValue=Wrap_Dress_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487310442496', newValue=Bodysuits_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074859364352', newValue=Blazers_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252349653385216', newValue=Knit_Tops_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487260110848', newValue=Jersey_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2251937252638720', newValue=Hoodie_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074809032704', newValue=Coats_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252074725146624', newValue=Jackets_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252349586276352', newValue=Cardigans_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252349770825728', newValue=Sweater_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252349603053568', newValue=Pullovers_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487025229824', newValue=T_Shirts_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487109115904', newValue=Crop_Top_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252487042007040', newValue=Tank_Tops_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252624682287104', newValue=Trousers_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252761936691200', newValue=Dress_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252761919913984', newValue=Party_Dress_l.rstrip())
add_houzhui(websiteId=websiteId, classificationId='2252762054131712', newValue=Skirt_l.rstrip())
"""
