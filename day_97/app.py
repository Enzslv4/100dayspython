from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Product, Order
import stripe

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # Simplified, use hashed passwords in real applications
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'danger')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cart')
@login_required
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get('cart', [])
    cart.append(product.id)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = session.get('cart', [])
    if request.method == 'POST':
        try:
            amount = sum(Product.query.get(item_id).price for item_id in cart_items)
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Stripe expects cents
                currency='usd',
                description='eCommerce purchase',
                source=request.form['stripeToken']
            )
            # Create order record
            order = Order(user_id=current_user.id, total_price=amount)
            db.session.add(order)
            db.session.commit()
            session.pop('cart', None)  # Clear cart after successful checkout
            flash('Your purchase was successful!', 'success')
            return redirect(url_for('index'))
        except stripe.error.StripeError:
            flash('There was an error processing your payment', 'danger')

    return render_template('checkout.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
