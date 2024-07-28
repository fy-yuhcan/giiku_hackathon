import React, { useState } from 'react';
import FoodHandler from './FoodHandler';
import Picture from './Picture';
import { FoodType } from '../materialType';
import { FoodProvider } from '../context/foodContext';

export default function AddFoodByImageComponent() {
    return (
      <>
        <FoodProvider>
          <Picture/>
          <FoodHandler/>
        </FoodProvider>
      </>
    );
}