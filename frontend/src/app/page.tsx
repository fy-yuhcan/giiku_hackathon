import React from 'react';
import Header from '../components/Header';
import RecipeSuggestion from '../components/RecipeSuggestion';
import { PageModeProvider } from '../context/pageContext';
import CenterComponent from '../components/CenterComponent';
import { UserProvider } from '../context/userContext';
import LoginComponent from '../components/LoginComponent';



const Home = () => {
  /*
  pageModeは
    "addFoodByImage", "addFoodByText"
    "addFood", "fridge", "home",
    "RecipeCreateAfter", "RecipeSuggestion"
  のどれか
  */

  //const [pageMode, setPageMode] = useState("home")
  return (
    <div>
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
    </div>
  );
};

export default Home;
