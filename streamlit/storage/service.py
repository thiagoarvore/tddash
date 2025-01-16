import streamlit as st

from . import repository


class BrandService:

    def __init__(self):
        self.brand_repository = repository.BrandRepository()

    def get_brands(self):
        if "brands" in st.session_state:
            return st.session_state.brands
        brands = self.brand_repository.get_brands()
        st.session_state.brands = brands
        return brands

    def create_brand(self, name):
        brand = dict(name=name)
        new_brand = self.brand_repository.create_brand(brand)
        st.session_state.brands.append(new_brand)
        return new_brand


class CategoryService:

    def __init__(self):
        self.category_repository = repository.CategoryRepository()

    def get_categories(self):
        if "categories" in st.session_state:
            return st.session_state.categories
        categories = self.category_repository.get_categories()
        st.session_state.categories = categories
        return categories

    def create_category(self, name):
        category = dict(name=name)
        new_category = self.category_repository.create_category(category)
        st.session_state.categories.append(new_category)
        return new_category


class SupplierService:

    def __init__(self):
        self.supplier_repository = repository.SupplierRepository()

    def get_suppliers(self):
        if "suppliers" in st.session_state:
            return st.session_state.suppliers
        suppliers = self.supplier_repository.get_suppliers()
        st.session_state.suppliers = suppliers
        return suppliers

    def create_supplier(self, name):
        supplier = dict(name=name)
        new_supplier = self.supplier_repository.create_supplier(supplier)
        st.session_state.suppliers.append(new_supplier)
        return new_supplier


class ProductService:

    def __init__(self):
        self.product_repository = repository.ProductRepository()

    def get_products(self):
        if "products" in st.session_state:
            return st.session_state.products
        products = self.product_repository.get_products()
        st.session_state.products = products
        return products

    def create_product(self, name, category, brand, serial_number, mac):
        product = dict(
            name=name,
            category=category,
            brand=brand,
            serial_number=serial_number,
            mac=mac,
        )
        new_product = self.product_repository.create_product(product)
        st.session_state.products.append(new_product)
        return new_product


class InflowService:

    def __init__(self):
        self.inflow_repository = repository.InflowRepository()

    def get_inflows(self):
        if "inflows" in st.session_state:
            return st.session_state.inflows
        inflows = self.inflow_repository.get_inflows()
        st.session_state.inflows = inflows
        return inflows

    def create_inflow(self, product, quantity, cost_price, supplier):
        inflow = dict(
            product=product,
            quantity=quantity,
            cost_price=cost_price,
            supplier=supplier,
        )
        new_inflow = self.inflow_repository.create_inflow(inflow)
        st.session_state.inflows.append(new_inflow)
        return new_inflow


class OutflowService:

    def __init__(self):
        self.outflow_repository = repository.OutflowRepository()

    def get_outflows(self):
        if "outflows" in st.session_state:
            return st.session_state.outflows
        outflows = self.outflow_repository.get_outflows()
        st.session_state.outflows = outflows
        return outflows

    def create_outflow(self, product, implemented, selling_price, quantity):
        outflow = dict(
            product=product,
            implemented=implemented,
            selling_price=selling_price,
            quantity=quantity,
        )
        new_outflow = self.outflow_repository.create_outflow(outflow)
        st.session_state.outflows.append(new_outflow)
        return new_outflow
