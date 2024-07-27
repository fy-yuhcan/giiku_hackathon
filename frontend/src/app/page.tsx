"use client";

import React, { useContext } from 'react';
import Header from '../components/Header';
import { PageModeProvider } from '../context/pageContext';
import CenterComponent from '../components/CenterComponent';
import { UserProvider } from '../context/userContext';
import LoginComponent from '../components/LoginComponent';
import { SuggestionRecipeIdContextProvider } from '../context/recipeContext';
import { UserContext } from '../context/userContext';


const Home = () => {
  /*
  pageModeは
    "addFoodByImage", "addFoodByText"
    "addFood", "fridge", "home",
    "RecipeCreateAfter", "RecipeSuggestion"
  のどれか
  */

  const { user } = useContext(UserContext)
  
  if ( true /* user.isLogin */) {
    return (
      <div>
      <SuggestionRecipeIdContextProvider>
      <UserProvider>
      <PageModeProvider>
        <div className="min-h-screen bg-yellow-100 flex flex-col justify-between">
          <Header />
            <main className="flex-grow flex flex-col items-center">
              <CenterComponent/>
            </main>
        </div>
      </PageModeProvider>
      </UserProvider>
      </SuggestionRecipeIdContextProvider>
    </div>
    )
  } else {
    return (
      <div>
      <LoginComponent></LoginComponent>
    </div>
    )
  }
};

export default Home;
