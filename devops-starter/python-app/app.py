from flask import Flask, jsonify, render_template, request, abort
import os


CATEGORIES = [
    "Power & Charging",
    "Productivity Essentials",
    "Connectivity & Expansion",
    "Travel Tech",
    "Keyboards",
    "Mice",
    "Accessories",
    "New Releases",
    "Best Sellers",
    "Discover / Explore",
]

PRODUCTS = [
    {
        "id": 1,
        "name": "GaN Fast Charger 100W",
        "model": "PC-100G",
        "category": "Power & Charging",
        "price": 89.99,
        "brand": "NovaTech",
        "connection": "Wired",
        "type": "Portable",
        "colors": ["Black", "Silver"],
        "rating": 4.8,
        "description": "Ultra-compact 4-port charger for laptops, tablets, and phones.",
        "features": ["100W USB-C PD", "2x USB-C + 2x USB-A", "Overheat protection"],
        "shipping": "Ships in 24 hours with 2-year warranty.",
    },
    {
        "id": 2,
        "name": "Wireless Ergo Keyboard",
        "model": "KB-E75",
        "category": "Keyboards",
        "price": 119.00,
        "brand": "NovaTech",
        "connection": "Wireless",
        "type": "Office",
        "colors": ["White", "Graphite"],
        "rating": 4.7,
        "description": "Low-profile ergonomic keyboard designed for long work sessions.",
        "features": ["Multi-device pairing", "Rechargeable battery", "Scissor switches"],
        "shipping": "Free shipping over $50.",
    },
    {
        "id": 3,
        "name": "Precision Pro Mouse",
        "model": "MS-PRO2",
        "category": "Mice",
        "price": 69.50,
        "brand": "Orbit",
        "connection": "Wireless",
        "type": "Gaming",
        "colors": ["Black", "Blue"],
        "rating": 4.6,
        "description": "High-precision sensor with programmable buttons for creators and gamers.",
        "features": ["26K DPI", "RGB lighting", "USB-C charging"],
        "shipping": "Next-day delivery available.",
    },
    {
        "id": 4,
        "name": "7-in-1 USB-C Hub",
        "model": "HB-7X",
        "category": "Connectivity & Expansion",
        "price": 59.99,
        "brand": "Dockly",
        "connection": "Wired",
        "type": "Portable",
        "colors": ["Space Gray"],
        "rating": 4.5,
        "description": "Expand your laptop with HDMI, USB-A, SD card, and power pass-through.",
        "features": ["4K HDMI", "100W pass-through", "SD/microSD reader"],
        "shipping": "Ships worldwide.",
    },
    {
        "id": 5,
        "name": "Travel Tech Organizer",
        "model": "TT-CASE",
        "category": "Travel Tech",
        "price": 39.00,
        "brand": "PackIQ",
        "connection": "Wired",
        "type": "Portable",
        "colors": ["Navy", "Black"],
        "rating": 4.4,
        "description": "Compact case for cables, adapters, chargers, and SSDs.",
        "features": ["Water-resistant", "Elastic compartments", "Slim profile"],
        "shipping": "Returns accepted within 30 days.",
    },
    {
        "id": 6,
        "name": "Aluminum Laptop Stand",
        "model": "LS-A2",
        "category": "Productivity Essentials",
        "price": 49.90,
        "brand": "NovaTech",
        "connection": "Wired",
        "type": "Office",
        "colors": ["Silver"],
        "rating": 4.9,
        "description": "Stable elevated stand that improves posture and airflow.",
        "features": ["Foldable", "Non-slip base", "Universal compatibility"],
        "shipping": "Dispatch within one business day.",
    },
]



def create_app() -> Flask:
    app = Flask(__name__)

    def nav_context():
        return {
            "menu_categories": CATEGORIES,
            "cart_count": 2,
        }

    @app.get("/")
    def index():
        return render_template(
            "home.html",
            featured=PRODUCTS[:4],
            new_arrivals=PRODUCTS[:3],
            best_sellers=sorted(PRODUCTS, key=lambda p: p["rating"], reverse=True)[:3],
            **nav_context(),
        )

    @app.get("/discover")
    def discover():
        return render_template("discover.html", products=PRODUCTS, **nav_context())

    @app.get("/search")
    def search():
        q = request.args.get("q", "").strip().lower()
        results = [p for p in PRODUCTS if q in p["name"].lower() or q in p["category"].lower()] if q else []
        return render_template("search.html", query=q, results=results, **nav_context())

    @app.get("/shop")
    def shop():
        category = request.args.get("category", "All")
        filtered = PRODUCTS
        if category != "All":
            filtered = [p for p in PRODUCTS if p["category"] == category]

        brand = request.args.get("brand")
        if brand:
            filtered = [p for p in filtered if p["brand"] == brand]

        connection = request.args.get("connection")
        if connection:
            filtered = [p for p in filtered if p["connection"] == connection]

        use_type = request.args.get("type")
        if use_type:
            filtered = [p for p in filtered if p["type"] == use_type]

        sort = request.args.get("sort")
        if sort == "price_asc":
            filtered = sorted(filtered, key=lambda p: p["price"])
        elif sort == "price_desc":
            filtered = sorted(filtered, key=lambda p: p["price"], reverse=True)
        elif sort == "best":
            filtered = sorted(filtered, key=lambda p: p["rating"], reverse=True)

        return render_template(
            "shop.html",
            products=filtered,
            selected_category=category,
            brands=sorted(set(p["brand"] for p in PRODUCTS)),
            **nav_context(),
        )

    @app.get("/product/<int:product_id>")
    def product_detail(product_id: int):
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if not product:
            abort(404)
        related = [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product_id][:3]
        return render_template("product.html", product=product, related=related, **nav_context())

    @app.get("/cart")
    def cart():
        cart_items = PRODUCTS[:2]
        subtotal = sum(item["price"] for item in cart_items)
        return render_template("cart.html", cart_items=cart_items, subtotal=subtotal, **nav_context())

    @app.route("/checkout", methods=["GET", "POST"])
    def checkout():
        message = ""
        if request.method == "POST":
            message = "Order confirmed! Thank you for shopping with us."
        return render_template("checkout.html", message=message, **nav_context())

    @app.get("/about")
    def about():
        return render_template("about.html", **nav_context())

    @app.route("/support", methods=["GET", "POST"])
    def support():
        sent = request.method == "POST"
        return render_template("support.html", sent=sent, **nav_context())

    @app.get("/rewards")
    def rewards():
        return render_template("rewards.html", **nav_context())

    @app.get("/accessibility")
    def accessibility():
        return render_template("legal.html", page_title="Accessibility Commitment", body="We are committed to WCAG-aligned improvements and inclusive shopping experiences.", **nav_context())

    @app.get("/privacy")
    def privacy():
        return render_template("legal.html", page_title="Privacy Policy", body="We collect only the data needed to process orders, improve service, and provide support.", **nav_context())

    @app.get("/terms")
    def terms():
        return render_template("legal.html", page_title="Terms & Conditions", body="By using our site, you agree to order, payment, and usage terms listed on this page.", **nav_context())

    @app.get("/shipping-returns")
    def shipping_returns():
        return render_template("legal.html", page_title="Shipping & Returns Policy", body="Standard delivery is 3-5 business days. Returns are accepted within 30 days in original condition.", **nav_context())

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/info")
    def info():
        return jsonify(
            {
                "version": os.getenv("APP_VERSION", "0.1.0"),
                "port": os.getenv("PORT", "8000"),
            }
        )

    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
