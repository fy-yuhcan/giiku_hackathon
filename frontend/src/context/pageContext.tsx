"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";


export type pageModeType = "addFoodByImage" | "addFood" | "fridge" | "home" |"RecipeCreateAfter"| "recipeSuggestion"
export type pageContextType = {
  pageMode: pageModeType;
  setPageMode: (pageMode: pageModeType) => void;
}


export const PageContext = createContext<pageContextType>({pageMode: "home", setPageMode: (pageMode) => pageMode});


export const PageModeProvider = ({children}) => {
    const [pageMode, setPageMode] = useState<pageModeType>("home")

  return (
    <PageContext.Provider value={{pageMode, setPageMode}}>
      {children}
    </PageContext.Provider>
  );
}
