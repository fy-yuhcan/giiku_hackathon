import React from 'react';
import FoodHandler from './FoodHandler';
import SmallButton from './SmallButton';
import Picture from './Picture';

export default function AddFoodByImageComponent() {
    
    return (
      <>
        <div>
          <Picture/>
          <FoodHandler/>
        </div>
      </>
    );
}