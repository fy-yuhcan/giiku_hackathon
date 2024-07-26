import React from 'react';
import FoodHandler from './FoodHandler';
import SmallButton from './SmallButton';
import { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';

export default function AddFoodByTextComponent() {
    const addFoodByImage: pageModeType = "addFoodByImage";

    return (
      <>
        <FoodHandler/>
        <SmallButton onClick={} label={"保存"}/>
      </>
    );
}