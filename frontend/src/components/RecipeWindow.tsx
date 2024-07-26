import React from 'react';

export default function RecipeWindow({ content }) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-3/4 max-w-lg mx-auto mt-10">
      <div className="text-left whitespace-pre-wrap">
        {content}
      </div>
    </div>
  );
}
