import React, { useState } from 'react';

function Order({ token }) {
  const [productID, setProductID] = useState('');

  const handleOrder = async () => {
    const response = await fetch('/order/', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ product_id: productID })
    });
    if (response.ok) {
      alert('Order placed successfully!');
    } else {
      alert('Error placing order');
    }
  };

  return (
    <div>
      <h2>Place an Order</h2>
      <input type="text" value={productID} onChange={(e) => setProductID(e.target.value)} placeholder="Product ID" />
      <button onClick={handleOrder}>Place Order</button>
    </div>
  );
}

export default Order;
