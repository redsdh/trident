
package com.tc.trident.support.dubbo;

import com.alibaba.dubbo.common.URL;
import com.alibaba.dubbo.common.bytecode.Proxy;
import com.alibaba.dubbo.common.bytecode.Wrapper;
import com.alibaba.dubbo.rpc.Invoker;
import com.alibaba.dubbo.rpc.proxy.AbstractProxyFactory;
import com.alibaba.dubbo.rpc.proxy.AbstractProxyInvoker;

/**
 *
 * @author kozz.gaof
 * @date Jan 11, 2015 9:13:55 PM
 * @id $Id$
 */
public class TridentProxyFactory extends AbstractProxyFactory {
    
    @SuppressWarnings("unchecked")
    public <T> T getProxy(Invoker<T> invoker, Class<?>[] interfaces) {
    
        return (T) Proxy.getProxy(interfaces).newInstance(new TridentInvokerInvocationHandler(invoker));
    }
    
    public <T> Invoker<T> getInvoker(T proxy, Class<T> type, URL url) {
    
        // TODO Wrapper类不能正确处理带$的类名
        final Wrapper wrapper = Wrapper.getWrapper(proxy.getClass().getName().indexOf('$') < 0 ? proxy.getClass() : type);
        return new AbstractProxyInvoker<T>(proxy, type, url) {
            
            @Override
            protected Object doInvoke(T proxy, String methodName,
                    Class<?>[] parameterTypes,
                    Object[] arguments) throws Throwable {
            
                return wrapper.invokeMethod(proxy, methodName, parameterTypes, arguments);
            }
        };
    }
    
}
