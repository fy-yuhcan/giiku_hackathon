"use client";

import React from 'react';
import { useState, createContext, ReactNode } from "react";

export type SuggestionRecipeIdType = {
  suggestionRecipeId: number;
  setSuggestionRecipeId: (pageMode: number) => void;
}

export const SuggestionRecipeIdContext = createContext<SuggestionRecipeIdType>({
    suggestionRecipeId: -1, 
    setSuggestionRecipeId: (suggestionRecipeId) => suggestionRecipeId
});

export const SuggestionRecipeIdContextProvider = ({children}) => {
    const [suggestionRecipeId, setSuggestionRecipeId] = useState<number>(-1)

  return (
    <SuggestionRecipeIdContext.Provider value={{suggestionRecipeId, setSuggestionRecipeId}}>
      {children}
    </SuggestionRecipeIdContext.Provider>
  );
}