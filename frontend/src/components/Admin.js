import React, { useState, useEffect } from 'react';

function Admin({ token }) {
  const [products, setProducts] = useState([]);
  const [newProduct, setNewProduct] = useState({ name: '', price: '', description: '' });

  useEffect(() => {
    fetch('/product/', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(response => response.json())
    .then(data => setProducts(data));
  }, [token]);

  const addProduct = async () => {
    const response = await fetch('/product/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newProduct)
    });
    if (response.ok) {
      const product = await response.json();
      setProducts([...products, product]);
    }
  };

  return (
    <div>
      <h1>Admin Panel</h1>
      <h2>Manage Products</h2>
      <div>
        <input type="text" placeholder="Product Name" value={newProduct.name} onChange={(e) => setNewProduct({ ...newProduct, name: e.target.value })} />
        <input type="number" placeholder="Price" value={newProduct.price} onChange={(e) => setNewProduct({ ...newProduct, price: e.target.value })} />
        <input type="text" placeholder="Description" value={newProduct.description} onChange={(e) => setNewProduct({ ...newProduct, description: e.target.value })} />
        <button onClick={addProduct}>Add Product</button>
      </div>

      <h2>Existing Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name} - ${product.price}</li>
        ))}
      </ul>
    </div>
  );
}

export default Admin;
