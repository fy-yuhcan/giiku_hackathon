import React from 'react';
import Image from 'next/image';
import Button from './Button';
import shokumaneImage from '../img/shokumane.png'; // 画像をインポート
import { pageModeType } from '../context/pageContext';

export default function HomeComponent() {
  const addFoodByImage: pageModeType = "addFoodByImage";
  const recipeSuggestion: pageModeType = "recipeSuggestion";

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-yellow-100">
      <Image src={shokumaneImage} alt="shokumane" className="mb-8" />
      <div className="space-y-4">
        <Button pageChangeTo={addFoodByImage} label={"食材の追加"} icon={"shopping-cart"} />
        <Button pageChangeTo={recipeSuggestion} label={"ごはんを作る"} icon={"utensils"} />
      </div>
    </div>
  );
}
