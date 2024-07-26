import React from 'react';
import { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';
import SmallButton from './SmallButton';

export default function RecipeSuggestion() {
  const {pageMode, setPageMode} = useContext(PageContext)
  const recipeDetailOne: pageModeType = "recipeDetailOne"
  
  const handleInputQuery = () => {

    /*apiたたく*/

    setPageMode(recipeDetailOne)
  }
  
  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">あなただけのレシピを作成します</h2>
      <textarea
        className="border rounded p-2 mb-4 w-1/2"
        placeholder="現在の気分や体調を入力してください あっさりしたものが食べたい気分 など…"
      ></textarea>
      <div className="flex items-center mb-4">
        <SmallButton handler={handleInputQuery} label={"作成!"}/>
        <label className="ml-2">
          <input type="checkbox" className="mr-1" />
          冷蔵庫にある食材のみを使う
        </label>
      </div>
    </div>
  );
}
