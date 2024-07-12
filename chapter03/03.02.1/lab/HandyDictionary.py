# Description: HandyDictionary implementation.
# Create a HandyDictionary in Python from the following C# example:
# using System;
# using System.Collections;
# using System.Collections.Generic;
# using System.Linq;

# namespace Copilot
# {
#     /// <summary>
#     /// Features:
#     /// - auto-generating values;
#     /// - auto-disposing IDisposable values that have left the dictionary;
#     /// </summary>
#     /// <typeparam name="KT">key type</typeparam>
#     /// <typeparam name="VT">value type</typeparam>
#     public class HandyDictionary<KT, VT> : IDisposable, IEnumerable<KeyValuePair<KT, VT>> //where VT: class
#     {
#         /// <summary>
#         /// Create HandyDictionary with auto-generating value function.
#         /// </summary>
#         /// <param name="getValue">method of creating an object for a key</param>
#         /// <param name="disposeValue">method of disposing a value</param>
#         public HandyDictionary(GetValue getValue, DisposeValue disposeValue = null)
#         {
#             this.getValue = getValue;
#             if (disposeValue != null)
#                 this.disposeValue = disposeValue;
#         }

#         /// <summary>
#         /// Method of creating an object for a key.
#         /// </summary>
#         /// <param name="key"></param>
#         /// <returns></returns>
#         public delegate VT GetValue(KT key);
#         protected GetValue getValue;

#         /// <summary>
#         /// Method of disposing a value.
#         /// </summary>
#         /// <param name="value"></param>
#         public delegate void DisposeValue(VT value);
#         /// <summary>
#         /// Method of disposing a value.
#         /// </summary>
#         protected DisposeValue disposeValue = delegate (VT value)
#         {
#             if (value != null && value is IDisposable)
#                 ((IDisposable)value).Dispose();
#         };

#         /// <summary>
#         /// Create HandyDictionary without auto-generating value function.
#         /// </summary>
#         /// <param name="defaultValue">the default value returned for an unset key</param>
#         /// <param name="disposeValue">method of disposing a value</param>
#         public HandyDictionary(VT defaultValue, DisposeValue disposeValue = null)
#         {
#             this.defaultValue = defaultValue;
#             if (disposeValue != null)
#                 this.disposeValue = disposeValue;
#         }
#         protected VT defaultValue;

#         /// <summary>
#         /// Create HandyDictionary without auto-generating value function.
#         /// </summary>
#         /// <param name="disposeValue">method of disposing a value</param>
#         public HandyDictionary(DisposeValue disposeValue = null)
#         {
#             defaultValue = default;
#             if (disposeValue != null)
#                 this.disposeValue = disposeValue;
#         }

#         /// <summary>
#         /// 
#         /// </summary>
#         ~HandyDictionary()
#         {
#             Dispose();
#         }

#         /// <summary>
#         /// 
#         /// </summary>
#         virtual public void Dispose()
#         {
#             //lock (this)
#             //{
#             //    if (keys2value != null)
#             //    {
#             Clear();
#             //        keys2value = null;
#             //    }
#             //}
#         }

#         /// <summary>
#         /// Clear the dictionary and dispose disposable elements.
#         /// </summary>
#         public void Clear()
#         {
#             lock (this)
#             {
#                 foreach (VT v in keys2value.Values)
#                     disposeValue(v);
#                 keys2value.Clear();
#             }
#         }
#         /// <summary>
#         /// Remove the element by the key and dispose it if disposable.
#         /// </summary>
#         /// <param name="key"></param>
#         public void Remove(KT key)
#         {
#             lock (this)
#             {
#                 if (keys2value.TryGetValue(key, out VT v))
#                     disposeIfUnique(v);
#                 keys2value.Remove(key);
#             }
#         }

#         void disposeIfUnique(VT value)
#         {
#             lock (this)
#             {
#                 if (value == null || !(value is IDisposable))
#                     return;
#                 int vKeyCount = 0;
#                 keys2value.Values.Where(a => a.Equals(value)).TakeWhile(a => ++vKeyCount < 2);
#                 if (vKeyCount < 2)//make sure it is the only inclusion of the object
#                     disposeValue(value);
#             }
#         }

#         /// <summary>
#         /// It is safe: returns default if does not exists.
#         /// To check for existance, use TryGetValue().
#         /// </summary>
#         /// <param name="key"></param>
#         /// <returns></returns>
#         public VT this[KT key]
#         {
#             get
#             {
#                 lock (this)
#                 {
#                     TryGetValue(key, out VT v);
#                     return v;
#                 }
#             }
#             set
#             {
#                 lock (this)
#                 {
#                     if (keys2value.TryGetValue(key, out VT v) && v != null && !v.Equals(value))
#                         disposeIfUnique(v);
#                     keys2value[key] = value;
#                 }
#             }
#         }
#         Dictionary<KT, VT> keys2value = new Dictionary<KT, VT>();

#         /// <summary>
#         /// 
#         /// </summary>
#         /// <returns></returns>
#         public IEnumerator<KeyValuePair<KT, VT>> GetEnumerator()
#         {
#             return keys2value.GetEnumerator();
#         }

#         IEnumerator IEnumerable.GetEnumerator()
#         {
#             return this.GetEnumerator();
#         }

#         /// <summary>
#         /// Actual key collection.
#         /// </summary>
#         public Dictionary<KT, VT>.KeyCollection Keys
#         {
#             get
#             {
#                 return keys2value.Keys;
#             }
#         }

#         /// <summary>
#         /// Actual value collection.
#         /// </summary>
#         public Dictionary<KT, VT>.ValueCollection Values
#         {
#             get
#             {
#                 return keys2value.Values;
#             }
#         }

#         /// <summary>
#         /// 
#         /// </summary>
#         /// <param name="key"></param>
#         /// <param name="value"></param>
#         /// <returns></returns>
#         public bool TryGetValue(KT key, out VT value)
#         {
#             if (!keys2value.TryGetValue(key, out value))
#             {
#                 if (getValue == null)
#                 {
#                     value = defaultValue;
#                     return false;
#                 }
#                 value = getValue(key);
#                 keys2value[key] = value;
#             }
#             return true;
#         }

#         /// <summary>
#         /// 
#         /// </summary>
#         /// <param name="key"></param>
#         /// <param name="value"></param>
#         public void Add(KT key, VT value)
#         {
#             this[key] = value;
#         }

#         /// <summary>
#         /// (!)The count can be implicitly changed by the auto-generating value function.
#         /// </summary>
#         public int Count
#         {
#             get
#             {
#                 return keys2value.Count;
#             }
#         }
#     }
# }

class HandyDictionary:
    def __init__(self, getValue, disposeValue=None):
        self.getValue = getValue
        if disposeValue is not None:
            self.disposeValue = disposeValue

    def __del__(self):
        self.Dispose()

    def Dispose(self):
        self.Clear()

    def Clear(self):
        for v in self.keys2value.values():
            self.disposeValue(v)
        self.keys2value.clear()

    def Remove(self, key):
        if key in self.keys2value:
            v = self.keys2value[key]
            self.disposeIfUnique(v)
            del self.keys2value[key]

    def disposeIfUnique(self, value):
        if value is None or not isinstance(value, IDisposable):
            return
        vKeyCount = 0
        for a in self.keys2value.values():
            if a == value:
                vKeyCount += 1
                if vKeyCount >= 2:
                    return
        self.disposeValue(value)

    def __getitem__(self, key):
        if key not in self.keys2value:
            if self.getValue is None:
                return self.defaultValue
            value = self.getValue(key)
            self.keys2value[key] = value
            return value
        return self.keys2value[key]

    def __setitem__(self, key, value):
        if key in self.keys2value:
            v = self.keys2value[key]
            if v is not None and v != value:
                self.disposeIfUnique(v)
        self.keys2value[key] = value

    def __iter__(self):
        return iter(self.keys2value.items())

    def Keys(self):
        return self.keys2value.keys()

    def Values(self):
        return self.keys2value.values()

    def TryGetValue(self, key):
        if key in self.keys2value:
            return True, self.keys2value[key]
        if self.getValue is None:
            return False, self.defaultValue
        value = self.getValue(key)
        self.keys2value[key] = value
        return True, value

    def Add(self, key, value):
        self[key] = value

    def Count(self):
        return len(self.keys2value)

    keys2value = {}