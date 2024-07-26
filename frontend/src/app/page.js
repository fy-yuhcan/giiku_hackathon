import React from 'react';
import Header from '../components/Header.js';
import FoodHandler from '../components/FoodHandler.js';
import { useState } from 'react';


const Home = () => {
  /*
  pageModeは
  "home", "fridge", "foodAdd"
  "foodAddByImage", "foodAddBytext"
  
  
  
  */

  const [pageMode, setPageMode] = useState("Home")
  return (
    <div className="min-h-screen bg-yellow-100 flex flex-col justify-between">
      <Header />
      <main className="flex flex-col items-center mt-10">
        <FoodHandler />
      </main>
    </div>
  );
};

export default Home;
