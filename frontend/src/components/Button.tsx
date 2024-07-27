import React, { useContext } from 'react';
import { PageContext } from '../context/pageContext';

export default function Button({ pageChangeTo, label, icon }) {
  const { setPageMode } = useContext(PageContext);

  const handlePageChange = () => {
    setPageMode(pageChangeTo);
  };



  return (
    <button
      onClick={handlePageChange}
      className="w-64 bg-white border border-gray-300 rounded-lg p-4 flex items-center justify-center space-x-2 hover:bg-gray-200 focus:outline-none shadow-md transition duration-300"
    >
      <span>{label}</span>
    </button>
  );
}
