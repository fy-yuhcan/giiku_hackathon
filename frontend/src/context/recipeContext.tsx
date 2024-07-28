"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";
import { RecipePostResponseType } from '../materialType';

export type RecipePostResponseContextType = {
  recipePostResponse: RecipePostResponseType;
  setRecipePostResponse: (recipePostResponse: RecipePostResponseType) => void;
}

export const RecipePostResponseContext = createContext<RecipePostResponseContextType>({
  recipePostResponse: null,
  setRecipePostResponse: (recipePostResponse) => recipePostResponse
});

export const RecipePostResponseProvider = ({children}) => {
    const [recipePostResponse, setRecipePostResponse] = useState<RecipePostResponseType>(null)

  return (
    <RecipePostResponseContext.Provider value={{recipePostResponse, setRecipePostResponse}}>
      {children}
    </RecipePostResponseContext.Provider>
  );
}