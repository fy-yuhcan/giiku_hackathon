import React, { useContext } from 'react';
import { PageContext, pageModeType } from '../context/pageContext';

const BackButton = ({ pageChangeTo }) => {
  const { setPageMode } = useContext(PageContext);

  const handleBack = () => {
    setPageMode(pageChangeTo);
  };

  return (
    <button onClick={handleBack} className="text-2xl font-bold p-2">
      &lt; 
    </button>
  );
};

export default BackButton;
