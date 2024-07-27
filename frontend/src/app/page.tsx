import React from 'react';
import Header from '../components/Header';
import RecipeSuggestion from '../components/RecipeSuggestion';
import { PageModeProvider } from '../context/pageContext';
import CenterComponent from '../components/CenterComponent';
import { UserProvider } from '../context/userContext';


const Home = () => {
  /*
  pageModeは
    "addFoodByImage", "addFoodByText"
    "addFood", "fridge", "home", 
    "recipeDetailOne", "RecipeSuggestion"
  のどれか
  */

  //const [pageMode, setPageMode] = useState("home")
  return (
    <div>
      <UserProvider>
      <PageModeProvider>
        <div className="min-h-screen bg-yellow-100 flex flex-col justify-between">
          <Header />
            <main className="flex flex-col items-center mt-10">
              <CenterComponent/>
            </main>
        </div>
      </PageModeProvider>
      </UserProvider>
    </div>
  );
};

export default Home;
