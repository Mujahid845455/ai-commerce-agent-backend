import uuid

from app.core.database import SessionLocal
from app.models.user import User
from app.models.merchant import Merchant
from app.models.product import Product
from app.models.cart import Cart, CartItem
from app.utils.security import hash_password

from seed_dataset import get_all_seed_products


def seed_database():
    db = SessionLocal()

    try:
        print("\n Starting AgentPay 1000+ Products Database Seed...\n")

        # ==========================================================
        # 1. USERS
        # ==========================================================

        customer = db.query(User).filter(User.email == "customer@agentpay.demo").first()

        if not customer:
            customer = User(
                name="Arjun Sharma",
                email="customer@agentpay.demo",
                password_hash=hash_password("Customer@123"),
                role="CUSTOMER"
            )
            db.add(customer)
            db.flush()
            print("[+] Customer created")
        else:
            print("[*] Customer already exists")

        merchant_user = db.query(User).filter(User.email == "merchant@agentpay.demo").first()

        if not merchant_user:
            merchant_user = User(
                name="AgentPay Sports Admin",
                email="merchant@agentpay.demo",
                password_hash=hash_password("Merchant@123"),
                role="MERCHANT"
            )
            db.add(merchant_user)
            db.flush()
            print("[+] Merchant user created")
        else:
            print("[*] Merchant user already exists")

        # ==========================================================
        # 2. MERCHANT
        # ==========================================================

        merchant = db.query(Merchant).filter(Merchant.owner_id == merchant_user.id).first()

        if not merchant:
            merchant = Merchant(
                owner_id=merchant_user.id,
                business_name="AgentPay MegaStore",
                description="AI-ready mega catalog for agentic commerce and AI buyers.",
                currency="INR"
            )
            db.add(merchant)
            db.flush()
            print("[+] Merchant profile created")
        else:
            print("[*] Merchant profile already exists")

        # ==========================================================
        # 3. 1000+ PRODUCTS SEED
        # ==========================================================

        products_data = get_all_seed_products()
        print(f"\n Seeding {len(products_data)} products into database...")

        # Load existing product names for fast checking
        existing_names = set(
            row[0] for row in db.query(Product.name).filter(Product.merchant_id == merchant.id).all()
        )

        new_products = []
        skipped_count = 0

        for data in products_data:
            if data["name"] in existing_names:
                skipped_count += 1
                continue

            product = Product(
                merchant_id=merchant.id,
                name=data["name"],
                description=data["description"],
                category=data["category"],
                price_paise=data["price_paise"],
                currency="INR",
                stock_quantity=data["stock_quantity"],
                attributes=data["attributes"],
                is_active=True
            )
            new_products.append(product)
            existing_names.add(data["name"])

        if new_products:
            db.bulk_save_objects(new_products)
            db.flush()
            print(f"[+] Successfully added {len(new_products)} new products!")

        if skipped_count > 0:
            print(f"[*] Skipped {skipped_count} existing products.")

        total_in_db = db.query(Product).filter(Product.merchant_id == merchant.id, Product.is_active == True).count()
        print(f" Total Active Products in Catalog: {total_in_db}")

        # ==========================================================
        # 4. CUSTOMER CART DEMO SETUP
        # ==========================================================

        cart = db.query(Cart).filter(Cart.user_id == customer.id, Cart.status == "ACTIVE").first()

        if not cart:
            cart = Cart(user_id=customer.id, status="ACTIVE")
            db.add(cart)
            db.flush()
            print("[+] Active customer cart created")
        else:
            print("[*] Active customer cart already exists")

        runner = db.query(Product).filter(Product.merchant_id == merchant.id, Product.name.ilike("%Campus Runner%")).first()

        if runner:
            existing_item = db.query(CartItem).filter(CartItem.cart_id == cart.id, CartItem.product_id == runner.id).first()
            if not existing_item:
                cart_item = CartItem(
                    cart_id=cart.id,
                    product_id=runner.id,
                    quantity=1,
                    unit_price_paise=runner.price_paise
                )
                db.add(cart_item)
                print("[+] Demo product added to cart")

        # ==========================================================
        # COMMIT
        # ==========================================================

        db.commit()

        print("\n" + "=" * 60)
        print(f" AGENTPAY DATABASE SEEDED WITH {total_in_db} PRODUCTS SUCCESSFULLY")
        print("=" * 60)
        print("Ready for AI Agent Search & Agentic Commerce\n")

    except Exception as e:
        db.rollback()
        print("\n SEED FAILED")
        print(str(e))
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()