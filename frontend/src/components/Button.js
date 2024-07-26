import React from 'react';

const Button = ({ label, icon }) => {
  return (
    <button className="bg-white border border-gray-300 rounded-lg p-4 flex items-center space-x-2">
      <span className="material-icons">{icon}</span>
      <span>{label}</span>
    </button>
  );
};

export default Button;
