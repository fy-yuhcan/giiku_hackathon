import React, { useState } from 'react';
import FoodHandler from './FoodHandler';
import Picture from './Picture';
import { FoodDataType } from '../materialType';

export default function AddFoodByImageComponent() {
  const [FoodData, setFoodData] = useState<FoodDataType[]>([]);

  return (
    <div className="flex justify-center items-start space-x-6 my-20">
      <Picture setFoodData={setFoodData} />
      <FoodHandler FoodData={FoodData} />
    </div>
  );
}
