import React, { useState } from 'react';
import FoodHandler from './FoodHandler';
import SmallButton from './SmallButton';
import Picture from './Picture';
import { FoodDataType } from '../materialType';

export default function AddFoodByImageComponent() {
    const [FoodData, setFoodData] = useState<FoodDataType[]>([])
    
    return (
      <>
        <div>
          <Picture setFoodData={setFoodData}/>
          <FoodHandler FoodData={FoodData}/>
        </div>
      </>
    );
}