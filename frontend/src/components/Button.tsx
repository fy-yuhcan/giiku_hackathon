import React from 'react';
import { useContext } from 'react';
import { PageContext } from '../context/pageContext';

export default function Button({pageChangeTo, label, icon}) {

  const {pageMode, setPageMode} = useContext(PageContext)

  const handlepageChange = () => {
    setPageMode(pageChangeTo)
  }
    return (
      <>
        <button onClick={handlepageChange} className="bg-white border border-gray-300 rounded-lg p-4 flex items-center space-x-2"/>
          <span className="material-icons"><img src={icon} alt={label}/></span>
          <span>{label}</span>
      </>
    );
};