"use client";

import React, { useState } from 'react';

export default function FoodHandler() {
  const [ingredients, setIngredients] = useState([
    { name: '', quantity: '', unit: 'g' },
  ]);

  const handleAddIngredient = () => {
    setIngredients([...ingredients, { name: '', quantity: '', unit: 'g' }]);
  };

  const handleChange = (index, field, value) => {
    const newIngredients = [...ingredients];
    newIngredients[index][field] = value;
    setIngredients(newIngredients);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('保存する食材:', ingredients);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <h2 className="text-2xl font-bold text-center mb-4">新しく追加する食材</h2>
      <form onSubmit={handleSubmit}>
        <div className="grid grid-cols-3 gap-4 mb-4">
          <label className="col-span-1 text-right">食材名</label>
          <label className="col-span-1 text-right">数</label>
          <label className="col-span-1 text-right">単位</label>
          {ingredients.map((ingredient, index) => (
            <React.Fragment key={index}>
              <input
                type="text"
                className="border rounded p-2 col-span-1"
                placeholder="食材名"
                value={ingredient.name}
                onChange={(e) => handleChange(index, 'name', e.target.value)}
              />
              <input
                type="number"
                className="border rounded p-2 col-span-1"
                placeholder="数"
                value={ingredient.quantity}
                onChange={(e) => handleChange(index, 'quantity', e.target.value)}
              />
              <select
                className="border rounded p-2 col-span-1"
                value={ingredient.unit}
                onChange={(e) => handleChange(index, 'unit', e.target.value)}
              >
                <option value="個">個</option>
                <option value="g">g</option>
                <option value="kg">kg</option>
                <option value="ml">ml</option>
                <option value="l">l</option>
                <option value="本">本</option>
                <option value="袋">袋</option>
              </select>
            </React.Fragment>
          ))}
        </div>
        <div className="text-center mb-4">
          <button
            type="button"
            className="bg-gray-200 border border-gray-300 rounded p-2"
            onClick={handleAddIngredient}
          >
            追加
          </button>
        </div>
        <div className="text-center">
          <button type="submit" className="bg-orange-500 text-white py-2 px-4 rounded">
            保存
          </button>
        </div>
      </form>
    </div>
  );
}
