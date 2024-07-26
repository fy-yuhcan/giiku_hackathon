import React, { useContext } from 'react';
import RecipeWindow from './RecipeWindow';
import SmallButton from './SmallButton';
import { PageContext, pageModeType } from '../context/pageContext';

export default function RecipeDetailOneComponent() {

    const content: string = "apiをたたいて参照した文字列"
    const recipeSuggestion: pageModeType = "recipeSuggestion"
    const {pageMode, setPageMode} = useContext(PageContext)
    
    const handleBack = () => {
      setPageMode(recipeSuggestion)
    }
    
    return (
      <>
        <RecipeWindow content={content}/>
        <SmallButton handler={handleBack} label={"戻る"}/>
      </>
    );
}