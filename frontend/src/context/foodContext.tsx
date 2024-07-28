"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";
import { FoodDataType } from '../materialType';


export type FoodContextType = {
  FoodData: FoodDataType[];
  setFoodData: (FoodData: FoodDataType[]) => void;
}


export const FoodContext = createContext<FoodContextType>({FoodData: [{
    food_id: 0,
    name: "",
    quantity: 0,
    unit: "g",
}], setFoodData: (FoodData) => FoodData});


export const FoodProvider = ({children}) => {
    const [FoodData, setFoodData] = useState<FoodDataType[]>([{
        food_id: 0,
        name: "",
        quantity: 0,
        unit: "g",
    }])

  return (
    <FoodContext.Provider value={{FoodData, setFoodData}}>
      {children}
    </FoodContext.Provider>
);
}