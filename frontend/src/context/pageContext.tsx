"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";


export type pageModeType =  "addFoodByImage" | "addFoodByText" |"addFood"| "fridge"| "home" |"recipeDetailOne"| "RecipeSuggestion"

export const PageContext = createContext("");


export const PageModeProvider = ({children}) => {
    const [pageMode, setPageMode] = useState<pageModeType>("home")

  return (
    <PageContext.Provider value={{pageMode, setPageMode}}>
      {children}
    </PageContext.Provider>
  );
}