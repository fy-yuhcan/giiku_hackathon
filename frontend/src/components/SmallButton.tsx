import React from 'react';

export default function SmallButton({ label, onClick }) {
  return (
    <button
      className="bg-gray-200 border border-gray-300 rounded py-1 px-3 text-sm hover:bg-gray-300"
      onClick={onClick}
    >
      {label}
    </button>
  );
}
