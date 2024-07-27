"use client";

import React, { useContext, useState } from 'react';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';
import internal from 'stream';

export type ingredientsType = {
  name: string,
  quantity: number,
  unit: "個" | "g" | "kg" | "ml" | "l" | "本" | "袋"
}

export default function FoodHandler() {
  const [ingredients, setIngredients] = useState<ingredientsType[]>([
    { name: '', quantity: 0, unit: 'g' },
  ]);

  //食材の追加
  const handleAddIngredient = () => {
    setIngredients([...ingredients, { name: '', quantity: 0, unit: 'g' }]);
  };

  //すでにある食材の変更
  const handleChange = (index: number, field: string, value: string|number) => {
    const newIngredients = [...ingredients];
    if (value === "quantity") {
      newIngredients[index][field] = parseFloat(value);
    } else {
      newIngredients[index][field] = value;
    }
    setIngredients(newIngredients);
  };

  //保存 & 冷蔵庫ページに移動
  const fridgePage: pageModeType = "fridge"
  const {pageMode, setPageMode} = useContext(PageContext)
  const handlePageChange = () => {
    setPageMode(fridgePage)
  }

  const fetcher = (url:string, method:string, body:{
    
  }) => {
    fetch(url, { 
      method: method,
      body: body
    })
    .then(res => res.json())
  }
  const handleSubmit = (event) => {
    handlePageChange()
  };


  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <h2 className="text-2xl font-bold text-center mb-4">新しく追加する食材</h2>
      <form>
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
          <SmallButton handler={handleSubmit} label={"保存"}/>
        </div>
      </form>
    </div>
  );
}
