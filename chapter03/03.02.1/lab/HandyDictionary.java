/**
 *  Description: HandyDictionary class implementation.
 * Create a HandyDictionary in Java from the following C# example:
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Copilot
{
    /// <summary>
    /// Features:
    /// - auto-generating values;
    /// - auto-disposing IDisposable values that have left the dictionary;
    /// </summary>
    /// <typeparam name="KT">key type</typeparam>
    /// <typeparam name="VT">value type</typeparam>
    public class HandyDictionary<KT, VT> : IDisposable, IEnumerable<KeyValuePair<KT, VT>> //where VT: class
    {
        /// <summary>
        /// Create HandyDictionary with auto-generating value function.
        /// </summary>
        /// <param name="getValue">method of creating an object for a key</param>
        /// <param name="disposeValue">method of disposing a value</param>
        public HandyDictionary(GetValue getValue, DisposeValue disposeValue = null)
        {
            this.getValue = getValue;
            if (disposeValue != null)
                this.disposeValue = disposeValue;
        }

        /// <summary>
        /// Method of creating an object for a key.
        /// </summary>
        /// <param name="key"></param>
        /// <returns></returns>
        public delegate VT GetValue(KT key);
        protected GetValue getValue;

        /// <summary>
        /// Method of disposing a value.
        /// </summary>
        /// <param name="value"></param>
        public delegate void DisposeValue(VT value);
        /// <summary>
        /// Method of disposing a value.
        /// </summary>
        protected DisposeValue disposeValue = delegate (VT value)
        {
            if (value != null && value is IDisposable)
                ((IDisposable)value).Dispose();
        };

        /// <summary>
        /// Create HandyDictionary without auto-generating value function.
        /// </summary>
        /// <param name="defaultValue">the default value returned for an unset key</param>
        /// <param name="disposeValue">method of disposing a value</param>
        public HandyDictionary(VT defaultValue, DisposeValue disposeValue = null)
        {
            this.defaultValue = defaultValue;
            if (disposeValue != null)
                this.disposeValue = disposeValue;
        }
        protected VT defaultValue;

        /// <summary>
        /// Create HandyDictionary without auto-generating value function.
        /// </summary>
        /// <param name="disposeValue">method of disposing a value</param>
        public HandyDictionary(DisposeValue disposeValue = null)
        {
            defaultValue = default;
            if (disposeValue != null)
                this.disposeValue = disposeValue;
        }

        /// <summary>
        /// 
        /// </summary>
        ~HandyDictionary()
        {
            Dispose();
        }

        /// <summary>
        /// 
        /// </summary>
        virtual public void Dispose()
        {
            //lock (this)
            //{
            //    if (keys2value != null)
            //    {
            Clear();
            //        keys2value = null;
            //    }
            //}
        }

        /// <summary>
        /// Clear the dictionary and dispose disposable elements.
        /// </summary>
        public void Clear()
        {
            lock (this)
            {
                foreach (VT v in keys2value.Values)
                    disposeValue(v);
                keys2value.Clear();
            }
        }
        /// <summary>
        /// Remove the element by the key and dispose it if disposable.
        /// </summary>
        /// <param name="key"></param>
        public void Remove(KT key)
        {
            lock (this)
            {
                if (keys2value.TryGetValue(key, out VT v))
                    disposeIfUnique(v);
                keys2value.Remove(key);
            }
        }

        void disposeIfUnique(VT value)
        {
            lock (this)
            {
                if (value == null || !(value is IDisposable))
                    return;
                int vKeyCount = 0;
                keys2value.Values.Where(a => a.Equals(value)).TakeWhile(a => ++vKeyCount < 2);
                if (vKeyCount < 2)//make sure it is the only inclusion of the object
                    disposeValue(value);
            }
        }

        /// <summary>
        /// It is safe: returns default if does not exists.
        /// To check for existance, use TryGetValue().
        /// </summary>
        /// <param name="key"></param>
        /// <returns></returns>
        public VT this[KT key]
        {
            get
            {
                lock (this)
                {
                    TryGetValue(key, out VT v);
                    return v;
                }
            }
            set
            {
                lock (this)
                {
                    if (keys2value.TryGetValue(key, out VT v) && v != null && !v.Equals(value))
                        disposeIfUnique(v);
                    keys2value[key] = value;
                }
            }
        }
        Dictionary<KT, VT> keys2value = new Dictionary<KT, VT>();

        /// <summary>
        /// 
        /// </summary>
        /// <returns></returns>
        public IEnumerator<KeyValuePair<KT, VT>> GetEnumerator()
        {
            return keys2value.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return this.GetEnumerator();
        }

        /// <summary>
        /// Actual key collection.
        /// </summary>
        public Dictionary<KT, VT>.KeyCollection Keys
        {
            get
            {
                return keys2value.Keys;
            }
        }

        /// <summary>
        /// Actual value collection.
        /// </summary>
        public Dictionary<KT, VT>.ValueCollection Values
        {
            get
            {
                return keys2value.Values;
            }
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="key"></param>
        /// <param name="value"></param>
        /// <returns></returns>
        public bool TryGetValue(KT key, out VT value)
        {
            if (!keys2value.TryGetValue(key, out value))
            {
                if (getValue == null)
                {
                    value = defaultValue;
                    return false;
                }
                value = getValue(key);
                keys2value[key] = value;
            }
            return true;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="key"></param>
        /// <param name="value"></param>
        public void Add(KT key, VT value)
        {
            this[key] = value;
        }

        /// <summary>
        /// (!)The count can be implicitly changed by the auto-generating value function.
        /// </summary>
        public int Count
        {
            get
            {
                return keys2value.Count;
            }
        }
    }
}
 */
public class HandyDictionary<KT, VT> implements AutoCloseable, Iterable<Map.Entry<KT, VT>> {
    private final Map<KT, VT> keys2value;
    private final Function<KT, VT> getValue;
    private final Consumer<VT> disposeValue;

    public HandyDictionary(Function<KT, VT> getValue, Consumer<VT> disposeValue) {
        this.getValue = getValue;
        this.disposeValue = disposeValue;
        this.keys2value = new HashMap<>();
    }

    public HandyDictionary(VT defaultValue, Consumer<VT> disposeValue) {
        this.getValue = null;
        this.disposeValue = disposeValue;
        this.keys2value = new HashMap<>();
    }

    public HandyDictionary(Consumer<VT> disposeValue) {
        this.getValue = null;
        this.disposeValue = disposeValue;
        this.keys2value = new HashMap<>();
    }

    @Override
    public void close() {
        clear();
    }

    public void clear() {
        synchronized (this) {
            keys2value.values().forEach(disposeValue);
            keys2value.clear();
        }
    }

    public void remove(KT key) {
        synchronized (this) {
            VT value = keys2value.get(key);
            if (value != null) {
                disposeIfUnique(value);
            }
            keys2value.remove(key);
        }
    }

    private void disposeIfUnique(VT value) {
        synchronized (this) {
            if (value == null || !(value instanceof AutoCloseable)) {
                return;
            }
            int vKeyCount = (int) keys2value.values().stream().filter(a -> a.equals(value)).limit(2).count();
            if (vKeyCount < 2) {
                disposeValue.accept(value);
            }
        }
    }

    public VT get(KT key) {
        synchronized (this) {
            VT value = keys2value.get(key);
            if (value == null && getValue != null) {
                value = getValue.apply(key);
                keys2value.put(key, value);
            }
            return value;
        }
    }

    public void put(KT key, VT value) {
        synchronized (this) {
            VT oldValue = keys2value.get(key);
            if (oldValue != null && !oldValue.equals(value)) {
                disposeIfUnique(oldValue);
            }
            keys2value.put(key, value);
        }
    }

    public int size() {
        return keys2value.size();
    }

    @Override
    public Iterator<Map.Entry<KT, VT>> iterator() {
        return keys2value.entrySet().iterator();
    }
}