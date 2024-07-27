import React from 'react';

export default function SmallButton({ handler, label }) {
  return (
    <button
      className="bg-white border border-gray-300 rounded-full py-1 px-4 text-sm hover:bg-gray-100 my-2"
      onClick={handler}
    >
      {label}
    </button>
  );
}
