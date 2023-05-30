`2693. Call Function with Custom Context`;

declare global {
  interface Function {
    callPolyfill(context: Record<any, any>, ...args: any[]): any;
  }
}

Function.prototype.callPolyfill = function (context, ...args): any {
  return this.apply(context, args);
};
