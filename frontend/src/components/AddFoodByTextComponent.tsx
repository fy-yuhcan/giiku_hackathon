import React from 'react';
import FoodHandler from './FoodHandler';
import SmallButton from './SmallButton';

export default function AddFoodByTextComponent() {
    const handleStoreFood = () => {
    }
    
    return (
      <>
        <FoodHandler/>
        <SmallButton onClick={handleStoreFood} label={"保存"}/>
      </>
    );
}