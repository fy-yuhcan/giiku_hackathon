"use client";

import React, { useContext, useState } from 'react';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';
import useSWRMutation from 'swr/mutation';
import { UserContext } from '../context/userContext';
import BackButton from './BackButton'; // BackButtonコンポーネントをインポート
import { FoodType } from '../materialType';
import { FoodContext } from '../context/foodContext';



export default function FoodHandler() {
  const  { FoodData, setFoodData } = useContext(FoodContext);

  //食材の追加
  const handleAddIngredient = () => {
    setFoodData([...FoodData, {food_id: 0, name: '', quantity: 0, unit: 'g' }]);
  };

  //すでにある食材の変更
  const handleChange = (index: number, field: string, value: string | number) => {
    const newFoodData = [...FoodData];
    if (field === "quantity") {
      newFoodData[index][field] = parseFloat(value);
    } else {
      newFoodData[index][field] = value;
    }
    setFoodData(newFoodData);
  };

  //保存 & 冷蔵庫ページに移動
  const fridgePage: pageModeType = "fridge";
  const home: pageModeType = "home"; // 遷移先のパスを指定
  const { setPageMode } = useContext(PageContext);

  const handlePageChange = () => {
    setPageMode(fridgePage);
  }


  //冷蔵庫に保存するフェッチ
  const {user, setUser} = useContext(UserContext)
  async function updateFridge(url:string, { arg }: {arg: {
      user_id: number,
      foods: {
          food_id: number,
          quantity: number
      }[]
  }}) {
    const res = await fetch(url, {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(arg)
    })
    return res.json()
  }


  const { trigger, isMutating } = useSWRMutation("http://127.0.0.1:8000/storage/", updateFridge)
  
  const handleSubmit = async () => {
    const foods = FoodData.map(ingredient => {return {food_id: ingredient.food_id, quantity: ingredient.quantity}})
    const data = {
      user_id: user.user_id, 
      foods: foods
    }
    await trigger(data)
    handlePageChange()
  };


  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <div className="absolute top-28 left-8">
        <BackButton pageChangeTo={home} /> {/* 戻るボタンを追加 */}
      </div>
      <h2 className="text-2xl font-bold text-center mb-4">新しく追加する食材</h2>
        <div className="grid grid-cols-3 gap-4 mb-4">
          <label className="col-span-1 text-right">食材名</label>
          <label className="col-span-1 text-right">数</label>
          <label className="col-span-1 text-right">単位</label>
          {FoodData.map((ingredient, index) => (
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
          <SmallButton handler={handleSubmit} label={"保存"} />
        </div>
    </div>
  );
}
