import React, { useEffect, useState } from 'react';

function Catalog({ token }) {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('/product/', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(response => response.json())
    .then(data => setProducts(data));
  }, [token]);

  return (
    <div>
      <h1>Product Catalog</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>{product.name} - ${product.price}</li>
        ))}
      </ul>
    </div>
  );
}

export default Catalog;
