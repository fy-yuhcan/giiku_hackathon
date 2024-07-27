import React from 'react';
import FoodHandler from './FoodHandler';
import SmallButton from './SmallButton';
import { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';

export default function AddFoodByTextComponent() {
    return (
      <>
        <FoodHandler/>
      </>
    );
}