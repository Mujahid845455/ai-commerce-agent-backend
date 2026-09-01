"""
AgentPay 1000+ Products Seed Dataset Generator
Covers 20 major e-commerce categories with detailed metadata and cross-sell relationships.
"""

def generate_mobiles():
    items = []
    # iPhone 15 & 16 Series
    iphone_models = [
        ("Apple iPhone 15", 79900, "Base iPhone 15 with Dynamic Island and 48MP camera"),
        ("Apple iPhone 15 Plus", 89900, "Large display iPhone 15 with all-day battery life"),
        ("Apple iPhone 15 Pro", 134900, "Titanium iPhone 15 Pro with A17 Pro chip and Action Button"),
        ("Apple iPhone 15 Pro Max", 159900, "Ultimate iPhone 15 Pro Max with 5x Telephoto camera"),
        ("Apple iPhone 16", 79900, "Next-gen iPhone 16 with Camera Control and Apple Intelligence"),
        ("Apple iPhone 16 Plus", 89900, "Big screen iPhone 16 with enhanced thermal performance"),
        ("Apple iPhone 16 Pro", 119900, "Grade 5 Titanium iPhone 16 Pro with 4K 120 fps Dolby Vision"),
        ("Apple iPhone 16 Pro Max", 144900, "Flagship iPhone 16 Pro Max with largest 6.9-inch display"),
    ]
    storages = [("128GB", 0), ("256GB", 10000), ("512GB", 30000)]
    colors = ["Black", "White", "Natural Titanium", "Desert Titanium", "Blue"]

    for name, base_price, desc in iphone_models:
        for st_name, st_add in storages:
            for color in colors[:3]:
                price = base_price + st_add
                items.append({
                    "name": f"{name} ({st_name}, {color})",
                    "description": f"{desc} with {st_name} storage in {color} finish.",
                    "category": "Mobiles & Smartphones",
                    "price_paise": price * 100,
                    "stock_quantity": 25,
                    "attributes": {
                        "brand": "Apple",
                        "mrp_paise": (price + 5000) * 100,
                        "rating": 4.8,
                        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=80",
                        "color": color,
                        "size": st_name,
                        "ai_tags": ["mobile", "smartphone", "iphone", "apple", "flagship", "cross_sell_case", "cross_sell_airpods", "cross_sell_powerbank"]
                    }
                })

    # Samsung Galaxy Series
    samsung_models = [
        ("Samsung Galaxy S24", 79999, "AI-powered flagship smartphone with ProVisual Engine"),
        ("Samsung Galaxy S24+", 99999, "QHD+ display flagship with Galaxy AI capabilities"),
        ("Samsung Galaxy S24 Ultra", 129999, "Ultimate Galaxy S24 Ultra with S Pen and 200MP camera"),
        ("Samsung Galaxy S25", 84999, "Next-generation Galaxy S25 with Snapdragon 8 Elite"),
        ("Samsung Galaxy S25 Ultra", 134999, "Top-of-the-line S25 Ultra with titanium frame and 100x Zoom"),
        ("Samsung Galaxy A35", 30999, "Awesome camera and Premium glass back mid-ranger"),
        ("Samsung Galaxy A55", 39999, "Metal frame mid-ranger with Knox Vault security"),
    ]
    for name, price, desc in samsung_models:
        for color in ["Phantom Black", "Marble Gray", "Amber Yellow"]:
            items.append({
                "name": f"{name} ({color})",
                "description": f"{desc} in {color}.",
                "category": "Mobiles & Smartphones",
                "price_paise": price * 100,
                "stock_quantity": 30,
                "attributes": {
                    "brand": "Samsung",
                    "mrp_paise": (price + 6000) * 100,
                    "rating": 4.7,
                    "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500&auto=format&fit=crop&q=80",
                    "color": color,
                    "size": "256GB",
                    "ai_tags": ["mobile", "smartphone", "samsung", "android", "galaxy", "cross_sell_case", "cross_sell_powerbank"]
                }
            })

    # OnePlus, Pixel, Xiaomi, Realme, Moto, Nothing
    others = [
        ("OnePlus 12 (16GB RAM, 512GB, Silky Black)", 64999, "OnePlus", "Flagship with Hasselblad camera and 100W SUPERVOOC charging."),
        ("OnePlus 12R (16GB RAM, 256GB, Cool Blue)", 45999, "OnePlus", "Performance phone with 4nm Snapdragon 8 Gen 2."),
        ("OnePlus Nord 4 (8GB RAM, 256GB, Oasis Green)", 32999, "OnePlus", "Metal unibody 5G phone with Snapdragon 7+ Gen 3."),
        ("OnePlus Nord CE 4 (8GB RAM, 128GB, Dark Chrome)", 24999, "OnePlus", "Everyday performance phone with 100W fast charge."),
        ("Google Pixel 8 (128GB, Hazel)", 75999, "Google", "Google AI phone with Best Take and Macro Focus."),
        ("Google Pixel 8 Pro (256GB, Obsidian)", 106999, "Google", "Pro camera system with Video Boost and Temperature Sensor."),
        ("Google Pixel 9 (256GB, Peony)", 79999, "Google", "Gemini AI integrated phone with Super Res Zoom."),
        ("Google Pixel 9 Pro (512GB, Hazel)", 109999, "Google", "Pro-grade triple camera with Pro Controls."),
        ("Xiaomi 14 (12GB RAM, 512GB, Black)", 69999, "Xiaomi", "Leica Summilux lens camera flagship."),
        ("Xiaomi 14 Civi (8GB RAM, 512GB, Cruise Blue)", 42999, "Xiaomi", "Cinematic dual selfie camera smartphone."),
        ("Redmi Note 13 Pro+ (12GB RAM, 512GB, Fusion Purple)", 31999, "Xiaomi", "200MP OIS camera with 120W HyperCharge."),
        ("Realme GT 6 (16GB RAM, 512GB, Fluid Silver)", 44999, "Realme", "AI flagship killer with 6000 nits Ultra Bright Display."),
        ("Realme 12 Pro+ (12GB RAM, 256GB, Submarine Blue)", 29999, "Realme", "Periscope portrait camera with luxury watch design."),
        ("Motorola Edge 50 Pro (12GB RAM, 256GB, Black Beauty)", 35999, "Motorola", "Pantone validated camera and 125W TurboPower."),
        ("Motorola G85 5G (12GB RAM, 256GB, Olive Green)", 18999, "Motorola", "3D Curved pOLED 120Hz display smartphone."),
        ("Nothing Phone 2 (12GB RAM, 512GB, Dark Grey)", 39999, "Nothing", "Glyph Interface phone with Snapdragon 8+ Gen 1."),
        ("Nothing Phone 2a (8GB RAM, 128GB, Milk)", 23999, "Nothing", "Unique transparent design with 50MP dual cameras."),
    ]
    for name, price, brand, desc in others:
        items.append({
            "name": name,
            "description": desc,
            "category": "Mobiles & Smartphones",
            "price_paise": price * 100,
            "stock_quantity": 20,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 4000) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["mobile", "smartphone", brand.lower(), "android", "cross_sell_case", "cross_sell_powerbank"]
            }
        })
    return items


def generate_laptops():
    items = []
    laptops = [
        ("MacBook Air M2 (8GB RAM, 256GB SSD, Midnight)", 99900, "Apple", "Ultra-thin laptop with M2 chip and 18-hour battery."),
        ("MacBook Air M2 (16GB RAM, 512GB SSD, Starlight)", 119900, "Apple", "M2 MacBook Air configured for heavy multitasking."),
        ("MacBook Air M3 (8GB RAM, 256GB SSD, Space Grey)", 114900, "Apple", "M3 chip MacBook Air with dual external display support."),
        ("MacBook Air M3 (16GB RAM, 512GB SSD, Midnight)", 134900, "Apple", "High performance M3 Air with Liquid Retina display."),
        ("MacBook Pro M3 (8GB RAM, 512GB SSD, Space Grey)", 169900, "Apple", "Pro laptop with M3 chip and XDR Liquid Retina display."),
        ("MacBook Pro M3 Pro (18GB RAM, 512GB SSD, Space Black)", 199900, "Apple", "Pro beast with M3 Pro chip and 18-core GPU."),
        ("Dell Inspiron 14 (Core i5 13th Gen, 16GB, 512GB SSD)", 56990, "Dell", "Reliable 14-inch laptop for daily productivity."),
        ("Dell Inspiron 15 (Core i7 13th Gen, 16GB, 1TB SSD)", 74990, "Dell", "15.6-inch laptop with FHD display and numeric keypad."),
        ("Dell XPS 13 (Intel Core Ultra 7, 16GB, 512GB SSD)", 139990, "Dell", "Premium CNC aluminium ultrabook with InfinityEdge display."),
        ("Dell XPS 15 (Core i9 13th Gen, 32GB, 1TB SSD, RTX 4060)", 249990, "Dell", "Creator powerhouse laptop with 3.5K OLED touch display."),
        ("HP Pavilion 14 (Core i5 13th Gen, 16GB, 512GB SSD)", 62990, "HP", "Lightweight metal body laptop with B&O audio."),
        ("HP Pavilion 15 (Ryzen 7 7730U, 16GB, 1TB SSD)", 68990, "HP", "Powerful AMD laptop for home and office work."),
        ("HP Victus 15 (Core i5 12th Gen, 16GB, 512GB, RTX 3050)", 63990, "HP", "Entry-level gaming laptop with 144Hz FHD display."),
        ("HP Victus 16 (Ryzen 7 7840HS, 16GB, 1TB, RTX 4060)", 98990, "HP", "High performance gaming laptop with OMEN Tempest cooling."),
        ("HP Spectre x360 14 (Intel Core Ultra 7, 16GB, 1TB OLED)", 164990, "HP", "2-in-1 convertible laptop with OLED touch screen and stylus."),
        ("Lenovo IdeaPad Slim 3 (Core i3 12th Gen, 8GB, 512GB SSD)", 35990, "Lenovo", "Budget friendly daily laptop for students."),
        ("Lenovo IdeaPad Slim 5 (Ryzen 7 7730U, 16GB, 512GB SSD)", 64990, "Lenovo", "Sleek aluminium laptop with FHD IPS display."),
        ("Lenovo LOQ (Core i5 12th Gen, 16GB, 512GB, RTX 3050 6GB)", 66990, "Lenovo", "Budget gaming laptop with AI Engine+ chip."),
        ("Lenovo Legion 5 Pro (Ryzen 7 7745HX, 32GB, 1TB, RTX 4070)", 159990, "Lenovo", "Esports gaming laptop with 16-inch WQXGA 240Hz screen."),
        ("ASUS VivoBook 15 (Core i5 13th Gen, 16GB, 512GB SSD)", 54990, "ASUS", "Slim and light laptop with Antibacterial Guard."),
        ("ASUS ZenBook 14 OLED (Intel Core Ultra 7, 16GB, 1TB SSD)", 109990, "ASUS", "Ultra-portable 1.2kg laptop with 3K 120Hz OLED screen."),
        ("ASUS ROG Strix G16 (Core i7 13th Gen, 16GB, 1TB, RTX 4060)", 139990, "ASUS", "Pro esports gaming laptop with Tri-Fan technology."),
        ("ASUS TUF Gaming F15 (Core i5 11th Gen, 16GB, 512GB, RTX 2050)", 49990, "ASUS", "Military-grade durable gaming laptop."),
        ("Acer Aspire 5 (Core i5 13th Gen, 16GB, 512GB SSD)", 48990, "Acer", "Versatile everyday laptop with aluminium top cover."),
        ("Acer Nitro V 15 (Core i5 13th Gen, 16GB, 512GB, RTX 4050)", 72990, "Acer", "Popular gaming laptop with AI noise reduction."),
        ("MSI Thin Gaming GF63 (Core i5 12th Gen, 16GB, 512GB, RTX 3050)", 52990, "MSI", "Ultra-thin 1.86kg gaming laptop."),
    ]
    for name, price, brand, desc in laptops:
        items.append({
            "name": name,
            "description": desc,
            "category": "Laptops",
            "price_paise": price * 100,
            "stock_quantity": 15,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 8000) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=80",
                "color": "Silver",
                "size": "14-inch",
                "ai_tags": ["laptop", "computer", brand.lower(), "cross_sell_bag", "cross_sell_mouse", "cross_sell_keyboard", "cross_sell_hub"]
            }
        })
    return items


def generate_audio():
    items = []
    audios = [
        ("Apple AirPods 3rd Gen", 19900, "Apple", "Spatial Audio earbuds with MagSafe Charging Case."),
        ("Apple AirPods Pro 2nd Gen (USB-C)", 24900, "Apple", "Active Noise Cancellation earbuds with Adaptive Audio."),
        ("Apple AirPods Max (Space Grey)", 59900, "Apple", "Over-ear wireless headphones with computational audio."),
        ("Samsung Galaxy Buds 2 Pro", 12999, "Samsung", "24-bit Hi-Fi audio TWS with 360 Audio."),
        ("Samsung Galaxy Buds FE", 6999, "Samsung", "Ergonomic fit wireless earbuds with Active Noise Cancellation."),
        ("OnePlus Buds 3", 5499, "OnePlus", "Dual driver TWS with 49dB Active Noise Cancellation."),
        ("OnePlus Buds Pro 2", 9999, "OnePlus", "Co-created with Dynaudio with Spatial Audio."),
        ("Sony WH-1000XM5 Wireless Headphones", 29990, "Sony", "Industry leading Noise Canceling over-ear headphones."),
        ("Sony WH-1000XM4 Wireless Headphones", 22990, "Sony", "Premium Noise Canceling headphones with Speak-to-Chat."),
        ("Sony WF-1000XM5 TWS Earbuds", 24990, "Sony", "Best noise canceling wireless earbuds with High-Res audio."),
        ("JBL Tune 510BT Wireless On-Ear Headphones", 2999, "JBL", "Pure Bass sound headphones with 40-hour battery."),
        ("JBL Tune 770NC ANC Headphones", 6499, "JBL", "Adaptive Noise Cancelling wireless over-ear headphones."),
        ("JBL Live 660NC Wireless Over-Ear ANC Headphones", 9999, "JBL", "Signature Sound headphones with Voice Assistant support."),
        ("JBL Flip 6 Portable Bluetooth Speaker", 9999, "JBL", "IP67 waterproof 2-way speaker system."),
        ("JBL Charge 5 Portable Speaker", 14999, "JBL", "Powerful sound speaker with built-in power bank."),
        ("Bose QuietComfort Wireless Headphones", 29900, "Bose", "Iconic quietness and comfortable over-ear headphones."),
        ("Bose SoundLink Flex Bluetooth Speaker", 15900, "Bose", "PositionIQ technology waterproof outdoor speaker."),
        ("Sennheiser Momentum 4 Wireless Headphones", 27990, "Sennheiser", "60-hour battery life headphones with audiophile sound."),
        ("boAt Rockerz 450 Wireless Bluetooth Headphones", 1499, "boAt", "40mm drivers, 15-hour playback on-ear headphones."),
        ("boAt Airdopes 141 TWS Earbuds", 1299, "boAt", "42-hour playtime earbuds with Beast Mode low latency."),
        ("Noise Buds VS102 Truly Wireless Earbuds", 1199, "Noise", "50-hour total playback with Instacharge technology."),
        ("Realme Buds Air 5 Pro TWS", 4999, "Realme", "Hi-Res LDAC audio with 50dB Active Noise Cancellation."),
    ]
    for name, price, brand, desc in audios:
        items.append({
            "name": name,
            "description": desc,
            "category": "Audio",
            "price_paise": price * 100,
            "stock_quantity": 40,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 2000) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["audio", "headphones", "earbuds", "speaker", brand.lower()]
            }
        })
    return items


def generate_wearables():
    items = []
    wearables = [
        ("Apple Watch Series 9 GPS 45mm", 44900, "Apple", "Advanced health sensors with Double Tap gesture."),
        ("Apple Watch SE 2nd Gen GPS 40mm", 24900, "Apple", "Essential fitness and safety features smartwatch."),
        ("Apple Watch Ultra 2 GPS + Cellular 49mm", 89900, "Apple", "Rugged outdoor sports smartwatch with 3000 nits display."),
        ("Samsung Galaxy Watch 6 44mm Bluetooth", 26999, "Samsung", "Advanced sleep tracking and personalized HR zones."),
        ("Samsung Galaxy Watch 6 Classic 47mm", 34999, "Samsung", "Rotating bezel smartwatch with BIA body composition sensor."),
        ("Google Pixel Watch 2 WiFi", 39900, "Google", "Fitbit tracking integrated with Google AI features."),
        ("OnePlus Watch 2 (Radiant Steel)", 24999, "OnePlus", "Dual-engine architecture with 100-hour battery life."),
        ("Amazfit GTR 4 Smartwatch", 16999, "Amazfit", "Dual-band GPS smartwatch with 150+ sports modes."),
        ("Amazfit GTS 4 Mini Smartwatch", 7999, "Amazfit", "Ultra-slim 9.1mm smartwatch with HD AMOLED display."),
        ("Garmin Forerunner 265 Running Smartwatch", 50490, "Garmin", "AMOLED display running smartwatch with Training Readiness."),
        ("Garmin Venu 3 GPS Smartwatch", 50990, "Garmin", "Advanced fitness and sleep coach smartwatch."),
        ("Fitbit Charge 6 Fitness Tracker", 14999, "Fitbit", "Health & fitness tracker with built-in GPS and Youtube Music control."),
        ("Noise ColorFit Pulse 3 Smartwatch", 1499, "Noise", "1.85-inch display smartwatch with Bluetooth calling."),
        ("boAt Wave Call 2 Smartwatch", 1299, "boAt", "1.83-inch HD display watch with DIY watch face studio."),
        ("Fire-Boltt Phoenix Pro Smartwatch", 1399, "Fire-Boltt", "Bluetooth calling smartwatch with 120+ sports modes."),
    ]
    for name, price, brand, desc in wearables:
        items.append({
            "name": name,
            "description": desc,
            "category": "Smartwatches & Wearables",
            "price_paise": price * 100,
            "stock_quantity": 30,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 3000) * 100,
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["wearable", "smartwatch", "fitness tracker", brand.lower()]
            }
        })
    return items


def generate_cameras():
    items = []
    cameras = [
        ("Canon EOS R50 Mirrorless Camera Body with 18-45mm Lens", 64995, "Canon", "Compact APS-C mirrorless camera for vlogging and photography."),
        ("Canon EOS R10 Mirrorless Camera Body with 18-150mm Lens", 92995, "Canon", "High speed 23fps RAW burst mirrorless camera."),
        ("Canon EOS R7 Mirrorless Camera Body", 127995, "Canon", "Advanced APS-C mirrorless with 32.5MP and in-body IS."),
        ("Canon PowerShot V10 Vlogging Camera", 34995, "Canon", "Pocket-sized 4K vlogging camera with built-in stand."),
        ("Nikon Z30 Mirrorless Camera Body with 16-50mm Lens", 59995, "Nikon", "Creator-focused 4K mirrorless camera with tally light."),
        ("Nikon Z50 Mirrorless Camera Body with 16-50mm Lens", 74995, "Nikon", "Ergonomic DX-format mirrorless camera with 20.9MP sensor."),
        ("Sony Alpha A6400 Mirrorless Camera with 16-50mm Lens", 78990, "Sony", "Real-time Eye AF 4K camera popular among content creators."),
        ("Sony Alpha A6700 Mirrorless Camera Body", 136990, "Sony", "Next-gen APS-C camera with AI processing unit and 4K 120p."),
        ("Sony Alpha A7 III Full-Frame Camera Body", 139990, "Sony", "Legendary full-frame camera with 24.2MP BSI sensor."),
        ("Sony Alpha A7 IV Full-Frame Camera Body", 222990, "Sony", "33MP hybrid full-frame camera with 4K 60p video."),
        ("GoPro HERO 12 Black Action Camera", 37990, "GoPro", "5.3K 60fps action camera with HyperSmooth 6.0 stabilization."),
        ("GoPro HERO 11 Black Action Camera", 31990, "GoPro", "Revolutionary 8:7 sensor action camera for social media creators."),
        ("DJI Osmo Action 4 Standard Combo", 33990, "DJI", "1/1.3-inch image sensor 4K 120fps waterproof action camera."),
        ("DJI Osmo Pocket 3 Gimbal Camera", 44990, "DJI", "1-inch CMOS pocket gimbal camera with 2-inch rotatable screen."),
        ("Fujifilm Instax Mini 12 Instant Camera (Pastel Blue)", 6499, "Fujifilm", "Fun instant camera with automatic exposure and selfie mode."),
    ]
    for name, price, brand, desc in cameras:
        items.append({
            "name": name,
            "description": desc,
            "category": "Cameras",
            "price_paise": price * 100,
            "stock_quantity": 12,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 5000) * 100,
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["camera", "photography", brand.lower(), "cross_sell_memorycard", "cross_sell_bag", "cross_sell_tripod"]
            }
        })
    return items


def generate_computer_accessories():
    items = []
    accessories = [
        ("Logitech MX Master 3S Wireless Mouse", 9995, "Logitech", "8K DPI track-on-glass silent wireless ergonomic mouse."),
        ("Logitech M330 Silent Plus Wireless Mouse", 1295, "Logitech", "90% noise reduction 2.4GHz wireless mouse."),
        ("Logitech G502 HERO High Performance Gaming Mouse", 3995, "Logitech", "HERO 25K sensor gaming mouse with 11 programmable buttons."),
        ("Logitech MX Keys S Wireless Mechanical Keyboard", 12995, "Logitech", "Fluid tactile typing low-profile illuminated keyboard."),
        ("Logitech K380 Multi-Device Bluetooth Keyboard", 2795, "Logitech", "Minimalist portable keyboard for Mac, Windows, iPad."),
        ("HP Wireless Mouse X200", 799, "HP", "Ambidextrous 1600 DPI 2.4GHz wireless mouse."),
        ("Dell KM3322W Wireless Keyboard and Mouse Combo", 1499, "Dell", "Anti-spill wireless desktop combo with 36-month battery life."),
        ("Razer DeathAdder V2 Ergonomic Gaming Mouse", 3499, "Razer", "20K DPI Focus+ optical sensor gaming mouse."),
        ("Razer BlackWidow V3 Mechanical Gaming Keyboard", 8999, "Razer", "Green mechanical switches keyboard with Chroma RGB."),
        ("Corsair K70 RGB PRO Mechanical Gaming Keyboard", 13999, "Corsair", "CHERRY MX Red mechanical switches with AXON hyper-processing."),
        ("Anker 7-in-1 USB-C Hub Adapter with 4K HDMI", 3999, "Anker", "100W Power Delivery USB-C hub with SD card reader."),
        ("UGREEN Aluminium Adjustable Laptop Stand", 1999, "UGREEN", "Ergonomic foldable desktop riser for laptops up to 17.3-inch."),
        ("Klim Wind RGB Laptop Cooling Pad (4 Fans)", 2499, "Klim", "High-speed 1200 RPM cooling pad for gaming laptops."),
        ("Logitech C920 HD Pro Webcam 1080p", 6995, "Logitech", "Full HD 1080p video calling webcam with dual stereo mics."),
        ("Blue Yeti USB Microphone for Streaming", 9995, "Logitech", "Multi-pattern condenser USB mic for podcasting and gaming."),
        ("Western Digital 2TB Elements External Hard Drive", 6299, "Western Digital", "Portable USB 3.0 external hard drive for data backup."),
        ("Samsung T7 1TB Portable External SSD", 9499, "Samsung", "Superfast 1050MB/s USB 3.2 Gen 2 portable SSD."),
        ("SanDisk Ultra 128GB USB 3.0 Flash Drive", 899, "SanDisk", "High-speed up to 130MB/s pen drive."),
        ("SanDisk Extreme 128GB MicroSD Card 190MB/s", 1499, "SanDisk", "A2 V30 4K UHD memory card for cameras and drones."),
        ("LG 24-inch IPS Full HD Borderless Monitor 75Hz", 9999, "LG", "FHD monitor with AMD FreeSync and Reader Mode."),
        ("Samsung Odyssey G5 27-inch WQHD Gaming Monitor 144Hz", 21999, "Samsung", "1000R Curved gaming monitor with 1ms response time."),
    ]
    for name, price, brand, desc in accessories:
        items.append({
            "name": name,
            "description": desc,
            "category": "Computer Accessories",
            "price_paise": price * 100,
            "stock_quantity": 50,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 1000) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["computer accessories", "accessory", brand.lower(), "tech"]
            }
        })
    return items


def generate_fashion_men():
    items = []
    categories = ["T-Shirts", "Shirts", "Jeans", "Trousers", "Jackets", "Running Shoes", "Sneakers", "Formal Shoes", "Wallets", "Belts", "Watches", "Backpacks", "Socks"]
    brands = ["AgentPay Sports", "Nike", "Puma", "Adidas", "Levi's", "Allen Solly", "Woodland", "Fastrack", "Tommy Hilfiger", "U.S. Polo Assn."]

    for i in range(120):
        brand = brands[i % len(brands)]
        cat = categories[i % len(categories)]
        price = 499 + (i * 120) % 4500
        items.append({
            "name": f"{brand} Men's {cat} Edition {i+1}",
            "description": f"Premium quality men's {cat.lower()} designed for comfort and durable daily wear.",
            "category": "Fashion — Men",
            "price_paise": price * 100,
            "stock_quantity": 40,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 500) * 100,
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1617137968427-85924c800a22?w=500&auto=format&fit=crop&q=80",
                "color": "Black" if i % 2 == 0 else "Blue",
                "size": "L" if i % 3 == 0 else "M",
                "ai_tags": ["fashion", "men", cat.lower(), brand.lower(), "clothing" if "Shoes" not in cat else "footwear", "cross_sell_socks" if "Shoes" in cat else "cross_sell_belt"]
            }
        })
    return items


def generate_fashion_women():
    items = []
    categories = ["Kurtis", "Sarees", "Dresses", "Tops", "Jeans", "Jackets", "Sneakers", "Heels", "Sandals", "Handbags", "Wallets", "Watches", "Scarves"]
    brands = ["Biba", "W for Woman", "Zara", "Mango", "H&M", "FabIndia", "Lavie", "Caprese", "Fossil", "Bata"]

    for i in range(120):
        brand = brands[i % len(brands)]
        cat = categories[i % len(categories)]
        price = 599 + (i * 130) % 5000
        items.append({
            "name": f"{brand} Women's {cat} Collection {i+1}",
            "description": f"Elegant women's {cat.lower()} with modern cuts and premium fabric finish.",
            "category": "Fashion — Women",
            "price_paise": price * 100,
            "stock_quantity": 35,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 600) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=500&auto=format&fit=crop&q=80",
                "color": "Pink" if i % 2 == 0 else "Maroon",
                "size": "M" if i % 2 == 0 else "S",
                "ai_tags": ["fashion", "women", cat.lower(), brand.lower(), "clothing" if "Handbags" not in cat else "accessories"]
            }
        })
    return items


def generate_home_kitchen():
    items = []
    appliances = [
        ("Prestige 750W Mixer Grinder 3 Jars", 2999, "Prestige"),
        ("Philips Cold Press Slow Juicer 150W", 11999, "Philips"),
        ("Kent 1.8L Stainless Steel Electric Kettle", 1199, "Kent"),
        ("Wonderchef 4.5L Digital Air Fryer", 4999, "Wonderchef"),
        ("IFB 25L Convection Microwave Oven", 12499, "IFB"),
        ("Pigeon 1800W Induction Cooktop", 1799, "Pigeon"),
        ("Prestige 3-Burner Glass Top Gas Stove", 4299, "Prestige"),
        ("Bajaj 2-Slice Pop-Up Toaster", 1399, "Bajaj"),
        ("Borosil Non-Stick Grill Sandwich Maker", 1699, "Borosil"),
        ("Morphy Richards Espresso Coffee Maker", 8999, "Morphy Richards"),
        ("Prestige 3L Hard Anodized Pressure Cooker", 1599, "Prestige"),
        ("Hawkins Triply Stainless Steel Frying Pan 24cm", 1899, "Hawkins"),
        ("Wonderchef Non-Stick Dosa Tawa 28cm", 999, "Wonderchef"),
        ("Milton Thermosteel 1L Water Bottle", 899, "Milton"),
        ("Solimo 100% Cotton King Bedsheet with 2 Pillow Covers", 899, "AmazonBasics"),
        ("Sleepwell Memory Foam Ergonomic Pillow", 1499, "Sleepwell"),
    ]
    for i in range(80):
        base_name, price, brand = appliances[i % len(appliances)]
        items.append({
            "name": f"{base_name} Model-{i+1}",
            "description": f"High durability home and kitchen product by {brand}.",
            "category": "Home & Kitchen",
            "price_paise": (price + i * 50) * 100,
            "stock_quantity": 25,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 800) * 100,
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=500&auto=format&fit=crop&q=80",
                "color": "Silver",
                "size": "Standard",
                "ai_tags": ["home", "kitchen", "cookware", "appliance", brand.lower()]
            }
        })
    return items


def generate_home_appliances():
    items = []
    appliances = [
        ("LG 242L 3 Star Smart Inverter Double Door Refrigerator", 25990, "LG"),
        ("Samsung 183L 4 Star Digital Inverter Single Door Refrigerator", 16990, "Samsung"),
        ("Bosch 7kg 5 Star Front Load Washing Machine", 31990, "Bosch"),
        ("LG 6.5kg 5 Star Smart Inverter Top Load Washing Machine", 17490, "LG"),
        ("Daikin 1.5 Ton 5 Star Inverter Split AC", 44990, "Daikin"),
        ("Voltas 1.5 Ton 3 Star Inverter Split AC", 32990, "Voltas"),
        ("Symphony 70L Desert Air Cooler", 10990, "Symphony"),
        ("Dyson V12 Detect Slim Cordless Vacuum Cleaner", 49900, "Dyson"),
        ("Eureka Forbes Wet & Dry Vacuum Cleaner 1400W", 7990, "Eureka Forbes"),
        ("Philips AC1215 Air Purifier for Home", 9990, "Philips"),
        ("Havells Stealth Air 1200mm Ceiling Fan", 3290, "Havells"),
        ("Wipro 12W Smart LED Bulb RGB (Pack of 4)", 1599, "Wipro"),
    ]
    for i in range(60):
        base_name, price, brand = appliances[i % len(appliances)]
        items.append({
            "name": f"{base_name} (Variant {i+1})",
            "description": f"Energy efficient home appliance engineered for modern homes.",
            "category": "Home Appliances",
            "price_paise": (price + i * 150) * 100,
            "stock_quantity": 15,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 3000) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=500&auto=format&fit=crop&q=80",
                "color": "White",
                "size": "Standard",
                "ai_tags": ["home appliance", "appliance", brand.lower()]
            }
        })
    return items


def generate_sports_fitness():
    items = []
    # Running gear
    running = [
        ("Campus Runner Pro", 1999, "AgentPay Sports", "Running Shoes", "Lightweight daily running shoes with cushioned sole.", ["cross_sell_socks", "cross_sell_bottle", "cross_sell_bag"]),
        ("Velocity Sprint 2", 2399, "AgentPay Sports", "Running Shoes", "Performance running shoes with responsive foam.", ["cross_sell_socks", "cross_sell_bottle"]),
        ("Asian Wonder Running Shoes", 2100, "Asian", "Running Shoes", "Breathable athletic shoes with flexible sole.", ["cross_sell_socks"]),
        ("Sparx Active X1", 1750, "Sparx", "Running Shoes", "Comfort focused running shoes for daily workouts.", ["cross_sell_socks"]),
        ("Premium Sports Socks (Pack of 3)", 299, "AgentPay Sports", "Sports Accessories", "Moisture wicking running socks.", ["running"]),
        ("Performance Water Bottle 750ml", 399, "AgentPay Sports", "Sports Accessories", "Leak resistant sports hydration bottle.", ["running"]),
        ("Lightweight Gym Backpack", 899, "AgentPay Sports", "Sports Accessories", "Compact water resistant workout bag.", ["running"]),
    ]
    for name, price, brand, subcat, desc, tags in running:
        items.append({
            "name": name,
            "description": desc,
            "category": "Sports & Fitness",
            "price_paise": price * 100,
            "stock_quantity": 45,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 400) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Regular",
                "ai_tags": ["sports", "fitness", subcat.lower(), brand.lower()] + tags
            }
        })

    # Gym, Cricket, Outdoor
    gym_cricket = [
        ("Decathlon Cast Iron Dumbbell Set 10kg", 2299, "Decathlon", "Dumbbells", "Pair of 5kg cast iron dumbbells for home workouts.", []),
        ("Kettlebell Rubber Coated 12kg", 1899, "Decathlon", "Gym", "Ergonomic wide grip kettlebell for strength training.", []),
        ("Resistance Band Set (5 Levels)", 699, "FitCore", "Gym", "Five level resistance band set with door anchor.", []),
        ("Nivia 15mm Extra Thick Yoga Mat", 999, "Nivia", "Gym", "Anti-slip eco-friendly NBR yoga and workout mat.", []),
        ("SG Club Leather Cricket Bat (Short Handle)", 2499, "SG", "Cricket", "English willow cricket bat with powerful sweet spot.", ["cross_sell_ball", "cross_sell_gloves", "cross_sell_pads", "cross_sell_kitbag"]),
        ("BDM Master Willow Cricket Bat", 3299, "BDM", "Cricket", "Handcrafted willow bat for tournament play.", ["cross_sell_ball", "cross_sell_gloves"]),
        ("SG Test Leather Cricket Ball (Pack of 6)", 1199, "SG", "Cricket", "Four-piece alum tanned leather cricket balls.", ["cricket"]),
        ("SS Matrix Cricket Batting Gloves", 899, "SS", "Cricket", "High-density foam padded cricket batting gloves.", ["cricket"]),
        ("SS Test Cricket Leg Guard Pads", 1999, "SS", "Cricket", "Lightweight moulded knee roll cricket pads.", ["cricket"]),
        ("SG Maxi Leather Cricket Kit Bag with Wheels", 2199, "SG", "Cricket", "Heavy duty nylon cricket kit bag with shoe compartment.", ["cricket"]),
        ("Yonex Astrox 88D Game Badminton Racket", 4499, "Yonex", "Rotational generator system power badminton racket.", []),
        ("Yonex Mavis 350 Nylon Shuttlecock (Pack of 6)", 999, "Yonex", "Precision manufactured nylon shuttlecocks.", []),
        ("Nivia Shining Star Leather Football (Size 5)", 899, "Nivia", "FIFA quality training football with 32 panels.", []),
    ]
    for gc_item in gym_cricket:
        name = gc_item[0]
        price = gc_item[1]
        brand = gc_item[2]
        subcat = gc_item[3]
        desc = gc_item[4]
        tags = gc_item[5] if len(gc_item) > 5 else []

        items.append({
            "name": name,
            "description": desc,
            "category": "Sports & Fitness",
            "price_paise": price * 100,
            "stock_quantity": 30,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 500) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["sports", "fitness", subcat.lower(), brand.lower()] + tags
            }
        })
    
    # Fill up to 100 items with generated variants
    for i in range(70):
        items.append({
            "name": f"Pro Fitness Gear Item #{i+1}",
            "description": f"High performance fitness accessory engineered for maximum endurance.",
            "category": "Sports & Fitness",
            "price_paise": (499 + i * 40) * 100,
            "stock_quantity": 25,
            "attributes": {
                "brand": "AgentPay Sports",
                "mrp_paise": (799 + i * 40) * 100,
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=80",
                "color": "Blue",
                "size": "Standard",
                "ai_tags": ["sports", "fitness", "gear"]
            }
        })
    return items


def generate_beauty_personal():
    items = []
    skincare = [
        ("Cetaphil Gentle Skin Cleanser 250ml", 599, "Cetaphil", "Hydrating facial cleanser for all skin types."),
        ("Minimalist 10% Niacinamide Face Serum 30ml", 599, "Minimalist", "Nourishing face serum for acne marks and texture."),
        ("Neutrogena Hydro Boost Water Gel 50g", 950, "Neutrogena", "Hyaluronic acid gel moisturizer."),
        ("Lotus Herbals UV Screen Matte Sunscreen SPF 50", 415, "Lotus", "Matte finish oil-free sunscreen lotion."),
        ("L'Oreal Professionnel Absolute Repair Shampoo 300ml", 795, "L'Oreal", "Protein enriched shampoo for damaged hair."),
        ("Kama Ayurveda Bringadi Intensive Hair Treatment Oil 100ml", 895, "Kama Ayurveda", "Traditional Ayurvedic hair regrowth oil."),
        ("Philips Beard Trimmer Series 3000 BT3211", 1499, "Philips", "Lift & Trim system stainless steel cordless trimmer."),
        ("Oral-B Pro 1000 Electric Rechargeable Toothbrush", 2499, "Oral-B", "CrossAction brush head electric toothbrush."),
        ("Braun All-in-One Trimmer Series 7 Grooming Kit", 4299, "Braun", "10-in-1 beard, hair and body grooming kit."),
    ]
    for i in range(60):
        name, price, brand, desc = skincare[i % len(skincare)]
        items.append({
            "name": f"{name} (Edition {i+1})",
            "description": desc,
            "category": "Beauty & Personal Care",
            "price_paise": (price + i * 20) * 100,
            "stock_quantity": 40,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 200 + i * 20) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=500&auto=format&fit=crop&q=80",
                "color": "N/A",
                "size": "Standard",
                "ai_tags": ["beauty", "personal care", brand.lower(), "skincare", "grooming"]
            }
        })
    return items


def generate_books_stationery():
    items = []
    books = [
        ("Python Crash Course 3rd Edition by Eric Matthes", 1499, "No Starch Press", "Best-selling hands-on introduction to Python programming."),
        ("Effective Java 3rd Edition by Joshua Bloch", 1899, "Addison-Wesley", "Definitive guide to Java platform best practices."),
        ("Eloquent JavaScript 4th Edition by Marijn Haverbeke", 1299, "No Starch Press", "Modern introduction to programming with JavaScript."),
        ("Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow", 2499, "O'Reilly", "Practical ML guide for building intelligent systems."),
        ("Designing Data-Intensive Applications by Martin Kleppmann", 2199, "O'Reilly", "Big data, distributed systems and architecture guide."),
        ("Atomic Habits by James Clear", 499, "Penguin", "Tiny changes, remarkable results self-help bestseller."),
        ("The Psychology of Money by Morgan Housel", 399, "Harriman", "Timeless lessons on wealth, greed, and happiness."),
        ("Rich Dad Poor Dad by Robert Kiyosaki", 399, "Plata", "What the rich teach their kids about money."),
        ("Sapiens: A Brief History of Humankind by Yuval Noah Harari", 499, "Vintage", "Exploration of human history and evolution."),
        ("Classmate Spiral Notebook 300 Pages (Pack of 3)", 349, "Classmate", "High quality unruled notebook set for notes."),
        ("Parker Vector Stainless Steel Rollerball Pen", 599, "Parker", "Classic chrome trim smooth writing pen."),
        ("Pilot V7 Hi-Tecpoint Pen 0.7mm (Pack of 5)", 399, "Pilot", "Liquid ink precision writing rollerball pens."),
    ]
    for i in range(60):
        name, price, publisher, desc = books[i % len(books)]
        items.append({
            "name": f"{name} Vol.{i+1}",
            "description": desc,
            "category": "Books & Stationery",
            "price_paise": price * 100,
            "stock_quantity": 50,
            "attributes": {
                "brand": publisher,
                "mrp_paise": (price + 200) * 100,
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500&auto=format&fit=crop&q=80",
                "color": "Multi",
                "size": "Standard",
                "ai_tags": ["books", "stationery", "reading", "programming", "learning"]
            }
        })
    return items


def generate_toys_kids():
    items = []
    toys = [
        ("LEGO Classic Large Creative Brick Box (790 Pieces)", 3999, "LEGO", "Creative building block set with 33 different colors."),
        ("LEGO City Police Station Playset", 5499, "LEGO", "3-level police station with patrol car and helicopter."),
        ("LEGO Technic McLaren Senna GTR Model", 4299, "LEGO", "Detailed V8 engine replica super sports car building set."),
        ("Hot Wheels 10-Car Gift Pack", 1199, "Hot Wheels", "1:64 scale die-cast vehicle collection."),
        ("RC Monster Truck 1:16 4WD Off-Road", 1899, "Hamleys", "High speed 2.4GHz remote control truck with rechargeable battery."),
        ("Barbie Dreamhouse 3-Story Dollhouse", 12999, "Mattel", "70+ accessories dollhouse with slide and pool."),
        ("Hasbro Monopoly Classic Board Game", 999, "Hasbro", "Classic fast-dealing property trading board game."),
        ("GAN 356 M 3x3 Magnetic Speed Rubik's Cube", 1999, "GAN", "Professional stickerless speed cube for cubers."),
        ("Skillmatics STEM Solar Robot 12-in-1 Kit", 1499, "Skillmatics", "Educational solar powered building robot kit for kids."),
        ("Chicco Baby Walker with Music & Lights", 3499, "Chicco", "Ergonomic multi-activity first steps baby walker."),
    ]
    for i in range(50):
        name, price, brand, desc = toys[i % len(toys)]
        items.append({
            "name": f"{name} Set #{i+1}",
            "description": desc,
            "category": "Toys & Kids",
            "price_paise": (price + i * 30) * 100,
            "stock_quantity": 25,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 400) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?w=500&auto=format&fit=crop&q=80",
                "color": "Multi",
                "size": "Standard",
                "ai_tags": ["toys", "kids", "games", "lego", brand.lower()]
            }
        })
    return items


def generate_grocery():
    items = []
    groceries = [
        ("Daawat Rozana Super Basmati Rice 5kg", 449, "Daawat", "Aromatic long grain basmati rice for daily meals."),
        ("Aashirvaad Select 100% MP Sharbati Atta 5kg", 329, "Aashirvaad", "Whole wheat flour made from premium Sharbati grains."),
        ("Tata Sampann Unpolished Toor Dal 1kg", 189, "Tata Sampann", "High protein unpolished arhar dal."),
        ("Fortune Sunlite Refined Sunflower Oil 5L Pouch", 699, "Fortune", "Light and healthy cooking oil enriched with vitamins."),
        ("Tata Salt Vacuum Evaporated Iodized Salt 1kg", 28, "Tata", "Purity tested iodized salt."),
        ("Cadbury Dairy Milk Silk Chocolate Bar 150g", 175, "Cadbury", "Rich, smooth and creamy milk chocolate."),
        ("Oreo Chocolate Cream Biscuits 300g", 90, "Oreo", "Crispy chocolate cookies with sweet vanilla cream."),
        ("Lays Classic Salted Potato Chips 100g", 50, "Lays", "Crispy sliced potato chips with sea salt."),
        ("Haldiram's Nagpur Bhujia Sev 400g", 120, "Haldiram's", "Traditional spicy gram flour crispy snack."),
        ("Maggi 2-Minute Masala Noodles (Pack of 12)", 168, "Maggi", "Iconic instant noodles with authentic Indian spices."),
        ("Tata Tea Gold Premium Black Tea 500g", 310, "Tata Tea", "Rich aroma black tea blend with 15% long leaves."),
        ("Nescafe Classic 100% Pure Instant Coffee 200g Glass Jar", 625, "Nescafe", "Rich roast instant coffee powder."),
        ("Twinings Green Tea Lemon & Honey (25 Tea Bags)", 380, "Twinings", "Refreshing blend of green tea with natural lemon."),
        ("Kellogg's Corn Flakes Original 875g", 370, "Kellogg's", "Crispy high iron breakfast cereal."),
        ("Quaker Whole Grain Rolled Oats 1kg", 199, "Quaker", "100% natural oats rich in dietary fiber."),
        ("Pintola All-Natural Peanut Butter Crunchy 1kg", 449, "Pintola", "Unsweetened high protein roasted peanut butter."),
        ("Dabur 100% Pure Natural Honey 500g Squeezy", 240, "Dabur", "Pure natural honey collected from forest hives."),
    ]
    for i in range(80):
        name, price, brand, desc = groceries[i % len(groceries)]
        items.append({
            "name": f"{name} Pack {i+1}",
            "description": desc,
            "category": "Grocery",
            "price_paise": price * 100,
            "stock_quantity": 100,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 30) * 100,
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1542838132-92c53300491e?w=500&auto=format&fit=crop&q=80",
                "color": "N/A",
                "size": "Standard",
                "ai_tags": ["grocery", "food", "staples", "snacks", brand.lower()]
            }
        })
    return items


def generate_automotive():
    items = []
    auto = [
        ("Spigen OneTap Magnetic Car Phone Holder (Dashboard)", 1999, "Spigen", "Strong N52 magnet dashboard car phone mount."),
        ("Anker 30W Dual USB Fast Car Charger", 1299, "Anker", "Compact metal alloy dual port fast car charger."),
        ("70mai Smart Dash Cam Pro Plus+ 1944P GPS", 6999, "70mai", "Dual-channel 2.7K dash camera with ADAS and Night Vision."),
        ("Portronics Auto Cleaner High Power Car Vacuum", 1499, "Portronics", "6000PA strong suction handheld car vacuum cleaner."),
        ("Godrej Aer Twist Car Air Freshener (Cool Surf Blue)", 349, "Godrej", "Long lasting 60-day twist car perfume."),
        ("3M Complete Car Care Kit (4 Items)", 1299, "3M", "Car shampoo, tyre dresser, dashboard polish and liquid wax."),
        ("Studds Ninja Elite Full Face Helmet (Black, L)", 1399, "Studds", "DOT certified ISI aerodynamic full face bike helmet."),
        ("Mototrance Heavy Duty Waterproof Bike Cover", 699, "Mototrance", "All weather dust and rain protection motorcycle cover."),
        ("Bobo BM4 Jaw Grip Bike Phone Mount with Charger", 1499, "Bobo", "Aluminium alloy vibration dampening bike phone holder."),
        ("Resqtech Digital Car Tyre Inflator 150 PSI", 2999, "Resqtech", "Auto cut-off heavy duty portable air compressor."),
        ("70mai 11100mAh Car Jump Starter Power Bank", 5499, "70mai", "Emergency peak 600A 12V car battery jump starter."),
    ]
    for i in range(50):
        name, price, brand, desc = auto[i % len(auto)]
        items.append({
            "name": f"{name} (V{i+1})",
            "description": desc,
            "category": "Automotive",
            "price_paise": price * 100,
            "stock_quantity": 30,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 400) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["automotive", "car", "bike", "accessories", brand.lower()]
            }
        })
    return items


def generate_electronics_accessories():
    items = []
    elec = [
        ("Mi 20000mAh 18W Fast Power Bank 3i", 2199, "Xiaomi", "Triple output port power bank with Power Delivery."),
        ("Anker 10000mAh Magnetic Wireless Power Bank", 4499, "Anker", "MagSafe compatible 15W wireless power bank for iPhone."),
        ("Anchor 4-Socket Power Strip with 2m Cord", 499, "Anchor", "Surge protection power board with master switch."),
        ("boAt Deuce USB-C to Lightning Cable 1.5m", 499, "boAt", "10000+ bend lifespan nylon braided fast charging cable."),
        ("Anker USB-C to USB-C 100W Cable 2m", 999, "Anker", "480Mbps data transfer 100W PD fast charge cable."),
        ("Samsung 25W USB-C Super Fast Wall Charger", 1299, "Samsung", "Official PPS fast adapter for Galaxy and Pixel phones."),
        ("Spigen ArcField 15W Wireless Charging Pad", 1999, "Spigen", "Qi certified fast wireless charger with AirBoost tech."),
        ("TP-Link Archer AX12 Wi-Fi 6 Dual-Band Router", 3299, "TP-Link", "Next-gen 1.5 Gbps Wi-Fi 6 gigabit router."),
        ("TP-Link RE305 AC1200 Wi-Fi Range Extender", 2199, "TP-Link", "Dual band Wi-Fi repeater with external antennas."),
        ("Wipro 16A Smart Plug with Energy Monitoring", 999, "Wipro", "Voice controlled Wi-Fi smart plug for AC & geyser."),
        ("Belkin Ultra High Speed 4K HDMI Cable 2m", 1499, "Belkin", "48Gbps 8K 60Hz / 4K 120Hz Dolby Vision HDMI 2.1 cable."),
    ]
    for i in range(60):
        name, price, brand, desc = elec[i % len(elec)]
        items.append({
            "name": f"{name} - Model {i+1}",
            "description": desc,
            "category": "Electronics & Accessories",
            "price_paise": price * 100,
            "stock_quantity": 40,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 300) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500&auto=format&fit=crop&q=80",
                "color": "Black",
                "size": "Standard",
                "ai_tags": ["electronics", "charger", "cable", "power bank", brand.lower()]
            }
        })
    return items


def generate_furniture():
    items = []
    furn = [
        ("Green Soul Monster Ultimate Ergonomic Gaming Chair", 16990, "Green Soul", "Premium breathable fabric gaming chair with 3D armrests."),
        ("Featherlite Liberate High Back Ergonomic Office Chair", 13500, "Featherlite", "Self-weight adjusting synchro tilt lumbar support chair."),
        ("DeckUp Renn Engineered Wood Study Table (Matte Finish)", 4299, "DeckUp", "Modern computer desk with storage shelves."),
        ("Green Soul Multi-Purpose Ergonomic Laptop Desk", 2499, "Green Soul", "Height adjustable mobile workstation table with wheels."),
        ("DeckUp Plank 5-Tier Wooden Bookshelf", 3899, "DeckUp", "Spacious open display bookcase for home and office."),
        ("Solimo 2-Door Engineered Wood Wardrobe with Mirror", 9999, "AmazonBasics", "Sturdy 2-door closet with hanging rod and shelves."),
        ("Nilkamal Freedom Mini Medium Plastic Shoe Cabinet", 2999, "Nilkamal", "Weatherproof 4-shelf plastic shoe storage rack."),
        ("Wakefit Orthopedic Teak Wood Queen Size Bed", 18999, "Wakefit", "Solid Sheesham teak wood bed with natural finish."),
        ("HomeTown 3-Seater Fabric Sofa (Grey)", 17999, "HomeTown", "High density foam cushioned living room sofa."),
        ("Durian Manual Fabric Recliner Chair", 21999, "Durian", "Plush padded single seater recliner sofa."),
    ]
    for i in range(50):
        name, price, brand, desc = furn[i % len(furn)]
        items.append({
            "name": f"{name} (Design {i+1})",
            "description": desc,
            "category": "Furniture",
            "price_paise": price * 100,
            "stock_quantity": 10,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 4000) * 100,
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&auto=format&fit=crop&q=80",
                "color": "Brown",
                "size": "Standard",
                "ai_tags": ["furniture", "chair", "table", "bed", "sofa", brand.lower()]
            }
        })
    return items


def generate_travel():
    items = []
    travel = [
        ("American Tourister 55cm Cabin Hard Trolley Suitcase", 3499, "American Tourister", "Scratch-resistant polypropylene 4-wheel Spinner luggage."),
        ("Skybags 65cm Medium Checked Hard Trolley Bag", 4299, "Skybags", "Lightweight poly-carbonate luggage with TSA combination lock."),
        ("Aristocrat 75cm Large Checked Hard Trolley", 3999, "Aristocrat", "Heavy duty expandable travel luggage."),
        ("Safari 45L Casual & Travel Backpack", 1499, "Safari", "3 compartment water-resistant polyester backpack."),
        ("Wildcraft 35L Work & Travel Laptop Backpack", 1899, "Wildcraft", "Padded 15.6-inch laptop compartment travel backpack."),
        ("Tommy Hilfiger Travel Duffel Bag 50L", 3999, "Tommy Hilfiger", "Premium canvas travel holdall bag."),
        ("DailyObjects Leather Passport Holder & Wallet", 999, "DailyObjects", "Genuine leather RFID blocking travel organizer."),
        ("Samsonite Memory Foam Ergonomic Travel Neck Pillow", 1999, "Samsonite", "Soft velvet cover cooling gel travel neck pillow."),
        ("Universal All-in-One World Travel Adapter 150+ Countries", 1299, "Anker", "Dual USB fast charging universal travel plug."),
    ]
    for i in range(50):
        name, price, brand, desc = travel[i % len(travel)]
        items.append({
            "name": f"{name} (Edition {i+1})",
            "description": desc,
            "category": "Travel",
            "price_paise": price * 100,
            "stock_quantity": 20,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 1000) * 100,
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1553531384-cc14c8086119?w=500&auto=format&fit=crop&q=80",
                "color": "Navy Blue",
                "size": "Medium",
                "ai_tags": ["travel", "luggage", "backpack", "suitcase", brand.lower()]
            }
        })
    return items


def generate_pet_supplies():
    items = []
    pets = [
        ("Pedigree Adult Dry Dog Food Chicken & Vegetables 10kg", 2299, "Pedigree", "Complete nutrition dry food for adult dogs."),
        ("Whiskas Adult Dry Cat Food Ocean Fish 3kg", 1199, "Whiskas", "Nutritious crunchy kibbles for adult cats."),
        ("Purepet Real Chicken Dog Crunchy Treats 500g", 349, "Purepet", "High protein baked reward dog treats."),
        ("Fida Heavy Duty Retractable Dog Leash 5m (up to 25kg)", 1299, "Fida", "One button brake & lock ergonomic dog leash."),
        ("Heads Up For Tails Padded No-Pull Dog Harness", 999, "HUFT", "Reflective nylon breathable mesh dog body harness."),
        ("Soft Plush Donut Pet Cushion Bed 60cm", 1499, "HUFT", "Calming self-warming round plush pet bed."),
        ("Trixie Interactive Cat Feather & Bell Toy", 499, "Trixie", "Engaging exercise wand toy for kittens and cats."),
        ("Wahl Odor Control Pet Shampoo 500ml", 699, "Wahl", "Eucalyptus & Spearmint natural formula dog shampoo."),
        ("AmazonBasics Foldable Soft-Sided Pet Carrier", 1899, "AmazonBasics", "Ventilated mesh travel bag for cats and small dogs."),
        ("Drools Clumping Lavender Cat Litter 10kg", 649, "Drools", "Fast clumping low dust bentonite cat litter."),
    ]
    for i in range(50):
        name, price, brand, desc = pets[i % len(pets)]
        items.append({
            "name": f"{name} Pack-{i+1}",
            "description": desc,
            "category": "Pet Supplies",
            "price_paise": price * 100,
            "stock_quantity": 30,
            "attributes": {
                "brand": brand,
                "mrp_paise": (price + 250) * 100,
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500&auto=format&fit=crop&q=80",
                "color": "Multi",
                "size": "Standard",
                "ai_tags": ["pet supplies", "dog food", "cat food", "pet toys", brand.lower()]
            }
        })
    return items


def get_all_seed_products():
    all_products = []
    all_products.extend(generate_mobiles())
    all_products.extend(generate_laptops())
    all_products.extend(generate_audio())
    all_products.extend(generate_wearables())
    all_products.extend(generate_cameras())
    all_products.extend(generate_computer_accessories())
    all_products.extend(generate_fashion_men())
    all_products.extend(generate_fashion_women())
    all_products.extend(generate_home_kitchen())
    all_products.extend(generate_home_appliances())
    all_products.extend(generate_sports_fitness())
    all_products.extend(generate_beauty_personal())
    all_products.extend(generate_books_stationery())
    all_products.extend(generate_toys_kids())
    all_products.extend(generate_grocery())
    all_products.extend(generate_automotive())
    all_products.extend(generate_electronics_accessories())
    all_products.extend(generate_furniture())
    all_products.extend(generate_travel())
    all_products.extend(generate_pet_supplies())
    return all_products
