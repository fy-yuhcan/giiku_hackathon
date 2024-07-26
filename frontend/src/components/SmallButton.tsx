import React from 'react';
import { useContext } from 'react';
import { PageContext } from '../context/pageContext';

export default function SmallButton({handler, label}) {

  return (
    <button
      className="bg-gray-200 border border-gray-300 rounded py-1 px-3 text-sm hover:bg-gray-300"
      onClick={handlepageChange}
    >
      {label}
    </button>
  );
}
