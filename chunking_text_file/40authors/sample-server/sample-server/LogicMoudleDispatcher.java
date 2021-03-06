// Generated by the fenrisulfr tools.  DO NOT EDIT!
package com.lz.game.game3.common.proto;
import cn.teaey.fenrisulfr.DispatcherHelper;
import cn.teaey.fenrisulfr.IDispatcher;
import cn.teaey.fenrisulfr.core.Fenrisulfr;
import com.google.inject.Inject;
import com.google.inject.Singleton;
import org.jboss.netty.channel.Channel;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * User: Teaey
 * Date: 13-6-17
 */
@Singleton
public class LogicMoudleDispatcher implements IDispatcher<Fenrisulfr.TransPacket>
{
    private static final Logger log = LoggerFactory.getLogger(GatewayMoudleDispatcher.class);

    @Inject
    private LogicLoginMoudleService logicLoginMoudleService;
    
    @Override
    public void diapatch(Channel channel, Fenrisulfr.TransPacket packet)
    {
        try
        {
            int opcode = packet.getOpcode();
            int moudle = DispatcherHelper.moudleType(opcode);
            switch (moudle)
            {
                case 1:
                    logicLoginMoudleService.diapatch(channel, packet);
                    break;
                default:
                    log.error("unknow moudle:{}", moudle);
                    break;
            }
        } catch (Exception e)
        {
            log.error("failed handle packet", e);
        }
    }
}
