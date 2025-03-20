import { Building2 } from 'lucide-react';

export function GovtLogo({ className }: { className?: string }) {
  return (
    <div className={`flex items-center ${className}`}>
      <Building2 className="h-8 w-8" />
      <div className="ml-2 flex flex-col">
        <span className="text-xs font-semibold">भारत सरकार</span>
        <span className="text-xs">Government of India</span>
      </div>
    </div>
  );
}